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
            send_comment_notifications.delay()
            
@task
def send_comment_notifications():
    print "sending email to %s" % subscriber.user.email 