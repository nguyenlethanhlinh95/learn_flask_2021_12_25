# syntax=docker/dockerfile:1
FROM python:3
WORKDIR /app
COPY ./app /app
#
ENV FLASK_APP=app.py
ENV PYTHONUNBUFFERED 1
ENV FLASK_ENV=development
ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000

CMD python app.py
