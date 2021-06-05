# blog-fastapi-ml

[Machine Learning real-time prediction using Docker & Python (FastAPI) by Zi-long QIU](https://scrat.academy/machine-learning-real-time-prediction-using-docker-and-python/)

## Requirements

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Installation

- Run `make up`
And then you can visit `http://localhost:80/`

## Commands

- `make up` (_full install_) run the project in docker and expose `http://localhost:80/`
- `make down` stop the project
- `make test` execute the tests (requirement: `make up` running)
- `make logs` allow to see the docker logs
- `make enter` allow to enter the php docker container

## Docker Services

| Name    | Image                                               | Port | Container           | Informations                                                                                  |
| ------- | --------------------------------------------------- | ---- | ------------------- | --------------------------------------------------------------------------------------------- |
| FastAPI ML | [tiangolo/uvicorn-gunicorn-fastapi:python3.8](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker) | 80 | blog-fastapi-ml   | Use `make enter` to enter the container                                                       |