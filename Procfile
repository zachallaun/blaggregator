web: gunicorn blaggregator.wsgi 
worker: celery -A blaggregator worker -l info 

crawlposts: python manage.py crawlposts
