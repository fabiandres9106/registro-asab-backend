from django.core.management.base import BaseCommand
from surveys.models import Function
from datetime import datetime

class Command(BaseCommand):
    help = 'Add predefined functions with date and time'

    def handle(self, *args, **kwargs):
        functions = [
            ('2024-06-06 19:00', 85),
            ('2024-06-07 19:00', 85),
            ('2024-06-08 19:00', 85),
            ('2024-06-09 17:00', 85),
            ('2024-06-10 17:00', 85),
        ]

        for func in functions:
            date_time_str, available_tickets = func
            date_time = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')
            Function.objects.create(date_time=date_time, available_tickets=available_tickets)

        self.stdout.write(self.style.SUCCESS('Successfully added functions'))