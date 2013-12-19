web: gunicorn blaggregator.wsgi 
worker: python manage.py celery worker -B

crawlposts: python manage.py crawlposts