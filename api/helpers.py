
from typing import List

from pydantic import BaseModel, ValidationError, validator
from ml.model import n_features

class PredictRequest(BaseModel):
    data: List[List[float]]

    @validator("data")
    def check_dimensionality(cls, v):
        for point in v:
            if len(point) != n_features:
                raise ValueError(f"Each data point must contain {n_features} features")

        return v

class PredictResponse(BaseModel):
    data: List[float]