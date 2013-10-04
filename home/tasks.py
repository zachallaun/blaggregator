from celery.task import Task, periodic_task
import requests
import os
import logging
from datetime import timedelta

class ZulipNewPost(Task):
    """ Notify Zulip that there is a new blog post. """
    
    def run(self, user, link, title):
        print "ZULIPING"
        stream = 'test-bot'
        key = os.environ.get('HUMBUG_KEY')
        email = os.environ.get('HUMBUG_EMAIL')

        subject = "new blog post: %s" % title
        subject = subject[:57] + "..."

        data = {
                    "type": "stream",
                    "to": "test-bot",
                    "subject": subject,
                    "content": "**%s** has a new blog post: [%s](%s)" % (user.first_name, title, link),
                }

        print "Here's what was sent to Zulip:", data['content']
        r = requests.post('https://humbughq-com-y3ee336dh1kn.runscope.net/api/v1/messages', data=data, auth=(email, key))
        return True
        
@periodic_task(run_every=timedelta(seconds=10))
def print_fib():
    logging.info('HELLO')
