FROM python:3.8-alpine

LABEL author="andrewnijmeh1@gmail.com"

WORKDIR /.

COPY requirements.txt .
RUN pip3 install -r requirements.txt

CMD ["python3", "polio.py"]
