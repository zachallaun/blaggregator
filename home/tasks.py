from celery.task import Task
import requests
import os

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

        print data['content']
        r = requests.post('https://humbughq-com-y3ee336dh1kn.runscope.net/api/v1/messages', data=data, auth=(email, key))
        return True