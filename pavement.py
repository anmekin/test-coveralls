import os

from paver.easy import task
from paver.easy import sh

@task
def test_tox():
    sh('pwd')
    sh('ls')
    sh('python cov/manage.py test cov/cov/test --settings=settings')