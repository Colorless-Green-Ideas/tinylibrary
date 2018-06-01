from fabric.api import cd, env, local, run, runs_once, settings, task

@task
def migrate():
    "run migrations locally"
    local('docker-compose  --log-level ERROR exec web pipenv run python manage.py migrate')


@task
def mk_migrations():
    "make migrations"
    local('docker-compose exec web pipenv run python manage.py makemigrations')