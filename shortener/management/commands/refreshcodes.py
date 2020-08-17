from django.core.management.base import BaseCommand, CommandError
from shortener.models import myURLSh

class Command(BaseCommand):
    help = 'Refreshes all myURLSh shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('items', type=int)

    def handle(self, *args, **options):
        return myURLSh.objects.refresh_shortcodes(items=options["items"])