from invoke import task

@task
def deps(c):
    c.run("docker pull node")

@task
def migrate(c):
    c.run("docker-compose run --rm web poetry run python manage.py migrate")

@task
def lint(c):
    c.run("pylint --ignore migrations")