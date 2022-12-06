FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt ./

RUN apt-get update

RUN pip install -U pip
RUN pip install -r requirements.txt
COPY . /app

ENV PYTHONPATH /app

EXPOSE 8080
CMD ["python3", "main.py"]
FROM asia.gcr.io/p4ds-team-2/p4ds-backend:latest
