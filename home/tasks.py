from __future__ import absolute_import
from blaggregator.celery import app
from celery import task
    
@task
def add(x, y):
    return x + y