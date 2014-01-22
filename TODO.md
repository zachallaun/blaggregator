Email notification feature: 
[x] When a new comment is created, create or update the commenter's subscription
[x] Enqueue task: takes a Comment object and a commenter. Queues up sendmail() tasks to everyone on the comment.posts's subscription list EXCEPT the commenter
[x] Need to write a migration script that loops over every post in the db and subscribes the author
[x] Make sure that it's sending to the subscription list that belongs to that specific post, NOT all the posts
[x] When a new POST is created, subscribe the author (move subscribe into function)
[x] add 'un/watch' link to /post
[ ] LEFT OFF HERE hook button up to a function that subscribes or unsubscribes people
[ ] internet: set up mailgun with jinja templating-
[ ] Ajax on un/watch button actions

[ ] test the 'subscribe author to comment thread' feature
[ ] once ready, on staging, run the self-subscribe script and check it

Important infrastructure:
[x] Get Celery working locally
[ ] Deploy Celery to Heroku (requires internet)
[ ] Upgrade logging (some notes in Trello, and Jorge's suggestions for settings.py config in Omnifocus)

Features that will drive engagement:
[ ] Track links clicked
[ ] Add email notifications of comments on your posts and replies to your comments
[ ] Add links to the discussion to the Zulip bot!
[ ] Weekly email of new posts and new comments