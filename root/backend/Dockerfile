FROM python:3.9-alpine

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

ENV PYTHONPATH /app

EXPOSE 8080
CMD ["python3", "main.py"]
