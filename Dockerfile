FROM python:3.11-slim-buster

WORKDIR /usr/src/send_sms_django_app

RUN apt update && apt upgrade -y && apt install -y build-essential libpq-dev

COPY . .

RUN pip install --upgrade && pip install -r requirements.txt



