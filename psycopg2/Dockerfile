FROM python:3.8-slim

ENV APP_HOME /app
WORKDIR $APP_HOME

RUN apt-get update
RUN apt-get install -y python3-dev
RUN apt-get install -y libpq-dev
RUN apt-get install -y gcc
RUN pip install psycopg2