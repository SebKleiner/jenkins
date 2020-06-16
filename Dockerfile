FROM python:3.6-jessie

WORKDIR /opt
ADD / /opt
RUN pip install -r requirements.txt
ENV URL_FILE=/home/ubuntu/url_list.txt

ENTRYPOINT python -u /opt/main_loop.py $URL_FILE