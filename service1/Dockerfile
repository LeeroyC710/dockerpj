FROM python:3.6.8-alpine

LABEL image for prize generation app flask application

WORKDIR /docker-flask

COPY . .

RUN pip install --upgrade pip 

RUN pip install -r requirements.txt

CMD python3 app.py
