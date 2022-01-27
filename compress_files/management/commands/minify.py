from django.core.management.base import BaseCommand
from django.db.models import Count
from datetime import timedelta, datetime

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print('Okayyyy')