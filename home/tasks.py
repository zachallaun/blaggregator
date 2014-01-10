from __future__ import absolute_import
from blaggregator.celery import app
from celery import task
from home.models import Comment_Subscription
    
@task
def add(x, y):
    return x + y
    
@task
def enqueue_comment_notification(commenter, comment): 
    subscriptions = Comment_Subscription.objects.filter(post=comment.post)
    for subscriber in subscriptions: 
        if subscriber.user != commenter: 
            send_comment_notification(subscriber.user, commenter, comment)
            
@task
def send_comment_notification(subscriber, commenter, comment):
    # todo actually send email 
    print "Now sending email to %s about comment %s by %s" % \
        (subscriber.email, comment, commenter)
