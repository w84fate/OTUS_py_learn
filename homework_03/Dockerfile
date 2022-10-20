FROM python:3.9-buster

EXPOSE 8000

WORKDIR /var/app

RUN pip install --upgrade pip

COPY . /var/app

RUN pip install -r requirements.txt

CMD uvicorn main:app --host 0.0.0.0