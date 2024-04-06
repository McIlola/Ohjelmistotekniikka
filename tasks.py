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
def start(ctx):
    ctx.run("python3 src/app.py", pty=True)

@task
def windows_test(ctx):
    ctx.run("pytest src", )

@task
def test(ctx):
    ctx.run("pytest src", pty=True)

@task
def windows_coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", )

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)
    if platform != "win32":
        call(("xdg-open", "htmlcov/index.html"))

@task(windows_coverage)
def windows_coverage_report(ctx):
    ctx.run("coverage html", )
    if platform != "win32":
        call(("xdg-open", "htmlcov/index.html"))