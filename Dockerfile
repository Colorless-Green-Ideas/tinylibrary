FROM python:3.7
MAINTAINER Jack Laxson <jack@getpizza.cat>

RUN mkdir -p /usr/src/tinylibrary /usr/share/cache/ && \
	chmod 777 /usr/share/cache/

COPY pyproject.toml poetry.lock /usr/src/tinylibrary/
WORKDIR /usr/src/tinylibrary/

RUN pip install poetry
RUN poetry install -v

COPY . /usr/src/tinylibrary/

RUN poetry install -v

EXPOSE 8000

HEALTHCHECK CMD curl -f http://localhost:8000/ || exit 1

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]