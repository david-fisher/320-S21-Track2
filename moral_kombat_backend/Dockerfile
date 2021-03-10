FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /app/api

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . ./

COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x ./wait-for-it.sh

EXPOSE 8000