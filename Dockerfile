# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /app
COPY ./app /app
#
ENV FLASK_APP=app.py
ENV PYTHONUNBUFFERED 1
ENV FLASK_ENV=development
ENV FLASK_RUN_HOST=0.0.0.0

RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000

CMD python app.py
