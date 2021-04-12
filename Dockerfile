FROM python:3.8

WORKDIR /

RUN pip3 install -r requirements.txt

RUN python3 polio.py 

