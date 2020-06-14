FROM python:3.6-jessie

WORKDIR /opt
ADD / /opt
RUN pip install -r requirements.txt

URLS=''

ENTRYPOINT python -u /opt/urls.py $URLS