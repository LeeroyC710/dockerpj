FROM python:3.6.8

WORKDIR /docker-flask

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD python3 app.py
