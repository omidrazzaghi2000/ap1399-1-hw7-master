FROM ubuntu:18.04
FROM gcc:9.2.0
FROM python:3.9.1-slim-buster

WORKDIR /usr/src/app

RUN apt-get update
RUN apt-get -y install --no-install-recommends build-essential libtbb-dev
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /var/cache/apt/*

ENV LD_LIBRARY_PATH="${LD_LIBRARY_PATH}"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["python","main.py"]