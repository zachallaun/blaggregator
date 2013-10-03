web: gunicorn blaggregator.wsgi
worker: python manage.py celery worker -B --loglevel=debug
crawlposts: python manage.py crawlposts
