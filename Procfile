web: gunicorn blaggregator.wsgi
worker: python manage.py celery worker --loglevel=debug
crawlposts: python manage.py crawlposts
