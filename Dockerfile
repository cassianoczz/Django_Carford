FROM python:3.10-slim-bullseye
WORKDIR /app
RUN python -m pip install Django pytest-cov
COPY . .