FROM python:3.9-alpine

RUN apk update && apk upgrade && apk add --no-cache --virtual libpq-dev python3-dev

RUN pip3 install --upgrade pip

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .