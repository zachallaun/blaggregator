from celery.task import Task, task, periodic_task
import requests
import os
# import logging
# from datetime import timedelta

class ZulipNewPost(Task):
    """ Notify Zulip that there is a new blog post. """
    
    def run(self, user, link, title):
        stream = 'test-bot' # todo: put back to announce
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
        
        if # todo: the post exists in the DB, may need to import models
            logging.debug("Zuliped:", data['content'])
            r = requests.post('https://humbughq-com-y3ee336dh1kn.runscope.net/api/v1/messages', data=data, auth=(email, key))
            return True
        else
            logging.error('Did not Zulip "%s"' % title)
            return False
@task
def sleeper():
    # TODO sleep for 5 minutes
    
    
    
    
        
# @periodic_task(run_every=timedelta(seconds=10))
# def testing_celerybeat():
#     logging.info('HELLO')
