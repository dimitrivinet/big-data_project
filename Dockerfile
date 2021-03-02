FROM ubuntu:18.04

RUN apt update &&\
    apt install -y python3-pip git && \
    pip3 install --upgrade pip

RUN pip3 install wheel sklearn flask pymongo

COPY app /app

CMD python3 app/app.py