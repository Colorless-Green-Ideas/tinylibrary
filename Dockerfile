FROM python:3.7
MAINTAINER Jack Laxson <jack@getpizza.cat>

RUN mkdir -p /usr/src/tinylibrary /usr/share/cache/ && \
	chmod 777 /usr/share/cache/

COPY Pipfile Pipfile.lock /usr/src/tinylibrary/
WORKDIR /usr/src/tinylibrary/

RUN pip install pipenv==2018.05.18
RUN pipenv sync -d

COPY . /usr/src/tinylibrary/

EXPOSE 8000

HEALTHCHECK CMD curl -f http://localhost:8000/ || exit 1

CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]