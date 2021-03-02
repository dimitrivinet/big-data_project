FROM ubuntu:18.04

RUN apt update && \
    apt install -y python3-pip git && \
     pip3 install --upgrade pip
RUN git clone https://github.com/dimitrivinet/toy_server.git
RUN pip3 install wheel
RUN pip3 install -r toy_server/requirements.txt

CMD bash