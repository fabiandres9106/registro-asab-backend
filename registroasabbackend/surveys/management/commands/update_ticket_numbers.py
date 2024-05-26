from django.core.management.base import BaseCommand
from surveys.models import SurveyResponse

class Command(BaseCommand):
    help = 'Assign unique ticket numbers to existing SurveyResponse records'

    def handle(self, *args, **kwargs):
        responses = SurveyResponse.objects.all()
        for response in responses:
            if response.ticket_number is None or response.ticket_number == 0:
                response.ticket_number = response.generate_unique_ticket_number()
                response.save()
        self.stdout.write(self.style.SUCCESS('Successfully updated ticket numbers for existing records'))