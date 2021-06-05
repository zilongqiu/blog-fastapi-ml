FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /app

COPY ./api /app

COPY ./requirements.txt /app
RUN pip install -r requirements.txt

EXPOSE 80

ENTRYPOINT ["/start-reload.sh"]