FROM python:3

ENV PYTHONUNBUFFERED 1
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD password

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

RUN pip freeze

COPY . /code/