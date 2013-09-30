[ ] redis is trying to connect to localhost even though it's on staging. look up how to configure it for production and edit settings.py

[ ] remove the dumb print statement after confirming that it's running. then change the stream name and try it on prod. switch the stream back to announce when done. 

[ ] can you make a holder stream and not start consuming it until the end of some process? ask jori

[ ] put initial account slurping into celery

[ ] configure some sort of emailer for email digests