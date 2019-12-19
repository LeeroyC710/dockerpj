FROM python:3.6.8

LABEL image for prize generation app flask application

WORKDIR /docker-flask

COPY . .

RUN ["pip3", "install", "pipenv"]

RUN [pip install -r requirements.txt]

CMD "pipenv run python main.py"

ENTRYPOINT ["/usr/local/bin/python", "app.py"]