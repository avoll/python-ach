FROM python:3.7-buster

ARG DEBIAN_FRONTEND=noninteractive

WORKDIR /app

ENV PIP_INDEX_URL https://nexus.earnup.com/repository/PyPI-All/simple
RUN pip install poetry==1.0.0b3
RUN poetry config virtualenvs.create false

COPY pyproject.toml .
COPY poetry.lock .

ENV PYTHONDONTWRITEBYTECODE=1

COPY . .

RUN poetry install
