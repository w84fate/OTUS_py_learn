#docker build . -t app
#docker run -it -p 8000:8000 app

FROM python:3.9-buster

EXPOSE 8000

WORKDIR /var/app

RUN pip install --upgrade pip

COPY requirements.txt /var/app

RUN pip install -r requirements.txt

COPY . /var/app

CMD uvicorn main:app --host 0.0.0.0