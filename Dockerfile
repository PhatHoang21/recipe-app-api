FROM python:3.7-alpine
MAINTAINER Phat Hoang

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# Create a new user for docker container to run our app.
# That is for security purpose.
RUN adduser -D user
USER user