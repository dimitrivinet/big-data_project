FROM ubuntu:18.04

RUN apt update && \
    apt install -y python3-pip git && \
     pip3 install --upgrade pip
RUN git clone https://github.com/dimitrivinet/toy_server.git
RUN pip3 install wheel sklearn flask

CMD bash