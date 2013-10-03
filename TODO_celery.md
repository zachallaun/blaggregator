Left off: 
I stuck a dumb job into crawlposts to test to see if it's working. 
It's working locally but not on Heroku (staging)
I installed the redis-to-go addon, which seems to be up and using memory
**** Right now I think it's the worker process that's not working. It shows up in the Procfile but not when I run heroku ps

DON'T FORGET TO PUSH TO THE MASTER BRANCH ON STAGING

Once I get this up and running I just need to write tasks to handle the stuff, and then test that and deploy! 

[ ] do i need more dynos?
[x] how do i get redis up and running on heroku?
[x] redis is trying to connect to localhost even though it's on staging. look up how to configure it for production and edit settings.py

[ ] remove the dumb print statement after confirming that it's running. then change the stream name and try it on prod. switch the stream back to announce when done. 

don't forget to reconfigure my procfile, don't need debug-level stuff

[ ] can you make a holder stream and not start consuming it until the end of some process? ask jori






[ ] put initial account slurping into celery

[ ] check github issues for other things that should be on celery

[ ] configure some sort of emailer for email digests