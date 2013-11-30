web: gunicorn blaggregator.wsgi && python manage.py celery worker -B

crawlposts: python manage.py crawlposts