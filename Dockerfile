FROM python:3.6-jessie

WORKDIR /opt
ADD / /opt
RUN pip install -r requirements.txt

ENV urls=https://www.infobae.com/america/

ENTRYPOINT python -u /opt/ulrs.py $urls