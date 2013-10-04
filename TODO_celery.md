[x] get celeryd running without errors
[x] get celerybeat running along with the daemon
[x] write sample periodic test to make sure celerybeat is running
[ ] delete extra print statements, 
add the super janky sleep task, and 
deploy the celery backend on prod! 
after deploy: 
  - don't forget to reconfigure my procfile, don't need debug-level stuff
  - don't forget to set stream back to 'announce'

DON'T FORGET TO PUSH TO THE MASTER BRANCH ON STAGING




Once I get this up and running I just need to write tasks to handle the stuff, and then test that and deploy! 

[ ] do i need more dynos? I think this means I'm now using 2 but I'm not sure. 

[ ] can you make a holder stream and not start consuming it until the end of some process? ask jori. I could always just have it queue up a job to sleep for 5 minutes at the beginning of the script, then make each job check to see if the post has been created yet. if not, delete the job. 

Notes for blog post: needed to scale the worker process on Heroku (and get the celerybeat up and running with in with the -b flag), plus migrate dj-celery forward with south. Show sample tasks.py file, things added to settings.py, and Procfile. Mention the different pieces I chose (Redis, redis-to-go)



[ ] put initial account slurping into celery

[ ] check github issues for other things that should be on celery

[ ] configure some sort of emailer for email digests. individual mailgun API calls or manage mailing lists and send one request to a list?