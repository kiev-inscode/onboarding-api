FROM python:3.10.12-slim

WORKDIR /library/

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .