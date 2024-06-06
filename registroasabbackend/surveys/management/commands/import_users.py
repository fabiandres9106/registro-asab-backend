import csv
from django.core.management.base import BaseCommand
from surveys.models  import Person, Ticket, EventDate

class Command(BaseCommand):
    help = 'Import users from a CSV file and generate tickets'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file to be processed')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        with open(csv_file, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Create or get the person
                person, created = Person.objects.get_or_create(
                    nombre=row['nombre'],
                    correo=row['correo'],
                    edad=row['edad'],
                    genero=row['genero'],
                    localidad=row['localidad'],
                    municipio_aledano=row['municipio_aledano'],
                    nivel_educativo=row['nivel_educativo'],
                    perfil_ocupacional=row['perfil_ocupacional'],
                    vinculacion_teatral=row['vinculacion_teatral'],
                    motivations=row['motivations'],
                    otras_motivaciones=row['otras_motivaciones'],
                    medio_informacion=row['medio_informacion'],
                    otros_eventos=row['otros_eventos'],
                    comprension_datos=row['comprension_datos'].lower() == 'true',
                    politica_datos=row['politica_datos'].lower() == 'true'
                )

                # Get the event
                event = EventDate.objects.get(id=row['event_id'])

                # Create the ticket
                Ticket.objects.create(
                    person=person,
                    event_date=event,
                    check_in=False  # Assuming the default value for check_in is False
                )

        self.stdout.write(self.style.SUCCESS('Successfully imported users and generated tickets.'))