FROM python:2.7
MAINTAINER Jack Laxson <jackjrabbit@gmail.com>

RUN mkdir -p /usr/src/tinylibrary

COPY requirements.txt /usr/src/tinylibrary/

RUN pip install --no-cache-dir -r /usr/src/tinylibrary/requirements.txt

COPY . /usr/src/tinylibrary/
WORKDIR /usr/src/tinylibrary/

EXPOSE 8000

CMD python2.7 manage.py runserver 0.0.0.0:8000