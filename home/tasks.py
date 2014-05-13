from __future__ import absolute_import
from blaggregator.celery_app import app
from celery import task
    
@app.task()
def add(x, y):
    return x + y