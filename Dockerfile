FROM python:3.9 AS requirements

COPY ./requirements /requirements
WORKDIR /requirements
RUN pip3 install -r /requirements/requirements.txt

FROM requirements as final

COPY ./api /app/api
COPY ./websocket /app/websocket
COPY ./service /app/service
COPY ./setup.py /app 

WORKDIR /app

RUN pip3 install .