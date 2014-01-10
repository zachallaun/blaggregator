'''
   One-time use: subscribe everyone to comment notifications on their own posts.
'''

from django.core.management.base import NoArgsCommand
from django.contrib.auth.models import User
from home.models import Post, Comment_Subscription
from django.core.exceptions import ObjectDoesNotExist

class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        
        if 'YES' == raw_input('\nDANGER DANGER DANGER.\nThis will subscribe everyone. Type YES if you want to continue. '):
            pass
            
            for post in Post.objects.all().iterator():
                user = post.blog.user
                subscription, created = Comment_Subscription.objects.get_or_create(
                    user = user,
                    post = post,
                )
                if created: print "Subscribed %s to %s" % (user, post)
                else: print "Confirmed %s to %s" % (user, post)
        else:
            print "OK, quitting without doing anything."
