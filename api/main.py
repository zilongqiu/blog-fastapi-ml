import numpy as np
import pandas as pd

from pprint import pprint
from io import BytesIO

from fastapi import FastAPI, File, UploadFile, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from ml.model import Model, get_model, n_features
from helpers import PredictRequest, PredictResponse

app = FastAPI()

# Simple prediction using array data
@app.post("/predict", response_model=PredictResponse)
def predict(input: PredictRequest, model: Model = Depends(get_model)):
    features = np.array(input.data)

    # Predict
    prediction = model.predict(features)
    result = PredictResponse(data=prediction.tolist())

    return result

# Simple prediction using csv data
@app.post("/predict_csv")
def predict_csv(csv_file: UploadFile = File(...), model: Model = Depends(get_model)):
    try:
        df = pd.read_csv(BytesIO(csv_file.file.read())).astype(float)
    except:
        raise HTTPException(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Unable to process file"
        )

    # Check if correct number of features
    df_n_instances, df_n_features = df.shape
    if df_n_features != n_features:
        raise HTTPException(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Each data point must contain {n_features} features",
        )

    # Predict
    prediction = model.predict(df.to_numpy().reshape(-1, n_features))
    result = PredictResponse(data=prediction.tolist())

    return result