from django.core.management.base import NoArgsCommand, CommandError
from django.core.mail import send_mail
from search.models import *

class Command(NoArgsCommand):
    help = 'Launches all researches'

    def handle_noargs(self, **options):
        send_mail('This is a test', 
                  'This is the message', 
                  'test', 
                  ['adilla.susungi@gmail.com'], 
                  fail_silently = False)
