from django.core.management.base import BaseCommand
from surveys.models import Event, EventDate, Theater
from datetime import datetime

class Command(BaseCommand):
    help = 'Add predefined data for Event, EventDate and Theater with date and time'

    def handle(self, *args, **kwargs):

        # Add Theater
        theater, created = Theater.objects.get_or_create(
            nombre="Teatro TECAL",
            defaults={
                "direccion": "Cl. 12b #2-27",
                "telefono": "3105867083",
                "contacto": "Mónica Camacho",
                "aforo": 80
            }
        )


        # Add Event
        event, created = Event.objects.get_or_create(
            teatro=theater,
            nombre_evento="Yo, Hedda Gabler",
            defaults={
                "direccion": "Rafael Alfonso Sánchez Gutiérrez",
                "produccion": "Facultad de Artes ASAB-UDFJ",
                "equipo_artistico": "Andres Felipe Barrero García, Alejandra Castro, Angela Natalia Trochez fuentes, Luisa Vargas, Ashly Camacho, Juan David Ayala Bohorquez, Juan Pablo Guzman Pulido"
            }
        )

        # Add EventDates
        event_dates = [
            {"date_time": '2024-06-06 19:00:00', "available_tickets": 80, "event": event},
            {"date_time": '2024-06-07 19:00:00', "available_tickets": 80, "event": event},
            {"date_time": '2024-06-08 19:00:00', "available_tickets": 80, "event": event},
            {"date_time": '2024-06-09 17:00:00', "available_tickets": 80, "event": event},
            {"date_time": '2024-06-10 17:00:00', "available_tickets": 80, "event": event},
        ]

        for event_date_data in event_dates:
            EventDate.objects.get_or_create(
                date_time=event_date_data["date_time"],
                event=event_date_data["event"],
                defaults={
                    "available_tickets": event_date_data["available_tickets"]
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully added functions'))