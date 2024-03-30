from invoke import task
from subprocess import call
from sys import platform

@task
def foo(ctx):
    print("bar")

@task
def windows_start(ctx):
    ctx.run("python src/app.py", )

@task
def linux_start(ctx):
    ctx.run("python3 src/app.py", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)
    if platform != "win32":
        call(("xdg-open", "htmlcov/index.html"))