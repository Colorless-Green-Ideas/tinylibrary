from fabric.api import cd, env, local, run, runs_once, settings, task

@task
def migrate():
    "run migrations locally"
    local('docker-compose  --log-level ERROR exec web pipenv run python manage.py migrate')

@task
def lint():
    with settings(warn_only=True):
        local("flake8 --count")
        local("eslint tinylibrary/static/tinylibrary/main.js tinylibrary/static/tinylibrary/tl-scanner.js tinylibrary/static/tinylibrary/quickrete-file.js")

@task
def mk_migrations():
    "make migrations"
    local('docker-compose exec web pipenv run python manage.py makemigrations')

@task
def debug():
    "We can use ipython 6+ on python3"
    local("docker-compose --log-level ERROR run -v$PWD/misc/ipython:/root/.ipython  --rm -u root web bash -c 'pipenv run pip install ipython && pipenv run python manage.py shell'")
