from django.core.management.base import NoArgsCommand, CommandError
from search.models import *
from apiclient.discovery import build
import pprint

class Command(NoArgsCommand):
    help = 'Launches all researches'

    def handle_noargs(self, **options):
        # service = build("customsearch", "v1",
        #                 developerKey="AIzaSyBGCWOxtQZomkXAVSLmyg1XI_obyTe5P4E")

        # res = service.cse().list(
        #     q='etudiant',
        #     cx='006966613857663466729:_k1q5ucd9eg',
        #     ).execute()
     #   pprint.pprint(res)
    #    test = open('/home/adilla/Bureau/test.txt', 'a')
    #    test.write('test')
    #    test.close()
