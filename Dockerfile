FROM python:3.6-jessie

WORKDIR /opt
ADD / /opt
RUN pip install -r requirements.txt

ENV NUMBER=6

ENTRYPOINT python, -u, /opt/main.py, $NUMBER