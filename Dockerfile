FROM python:3.8.18

RUN apt-get upgrade && apt-get update

COPY requirements.txt /app/requirements.txt

RUN pip install -U pip

RUN pip install -r /app/requirements.txt

COPY . /app

WORKDIR /app

EXPOSE 8000

CMD [ "python", "manage.py", "runserver" ]