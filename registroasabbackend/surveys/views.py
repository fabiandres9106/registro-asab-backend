from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
from django.http import JsonResponse, HttpResponseBadRequest
from .models import Event, EventDate, Person, Ticket
from .serializers import EventSerializer, EventDateSerializer, PersonSerializer, TicketSerializer
from datetime import datetime
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer
import csv
from django.http import HttpResponse
import locale
from babel.dates import format_datetime
from pytz import timezone
from .utils import send_confirmation_email


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

def hola_mundo(request):
    return JsonResponse({"mensaje": "hola_mundo"})

class EventListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.AllowAny]

class EventDetailView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.AllowAny]

class EventDateListView(generics.ListAPIView):    
    serializer_class = EventDateSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        event_id = self.kwargs['event_id']
        return EventDate.objects.filter(event_id=event_id)
    
class EventDateDetailView(generics.RetrieveAPIView):
    queryset = EventDate.objects.all()
    serializer_class = EventDateSerializer
    permission_classes = [permissions.AllowAny]

class PersonListView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [permissions.AllowAny]

class PersonDetailView(generics.RetrieveAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [permissions.AllowAny]

class TicketListView(generics.ListCreateAPIView):
    serializer_class = TicketSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        data = request.data
        person_id = data.get('person')
        event_date_id = data.get('event_date')

        try:
            person = Person.objects.get(id=person_id)
            event_date = EventDate.objects.get(id=event_date_id)
        except (Person.DoesNotExist, EventDate.DoesNotExist) as e:
            return HttpResponseBadRequest(str(e))

        ticket = Ticket(
            person=person,
            event_date=event_date
        )
        ticket.save()

        return JsonResponse({'message': 'Ticket created successfully!', 'ticket_number': ticket.ticket_number}, status=201)

    def get_queryset(self):
        event_date = self.kwargs['event_date']
        return Ticket.objects.filter(event_date=event_date)
    
    
class TicketDetailView(generics.RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [permissions.AllowAny]

class TicketUpdateView(generics.UpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [permissions.AllowAny] #Hace falta definir los roles los cuales tienen permitido hacer Update

def export_tickets_csv(request):
    # Crear una respuesta HTTP con el tipo de contenido CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="tickets.csv"'

    writer = csv.writer(response)
    # Escribir la cabecera del CSV
    writer.writerow(['Nombre', 'Correo', 'Edad', 'Genero', 'Localidad', 'Municipio Aledaño', 'Nivel Educativo', 'Perfil Ocupacional', 'Vinculacion Teatral', 'Motivaciones', 'Otras Motivaciones', 'Medio Informacion', 'Otros Eventos', 'Comprension Datos', 'Politica Datos', 'Numero de Ticket', 'Fecha de Funcion', 'Check-in'])
    permission_classes = [permissions.AllowAny] #Hace falta definir los roles los cuales tienen permitido hacer Update

    # Obtener todos los tickets y escribir los datos en el CSV
    tickets = Ticket.objects.select_related('person', 'event_date')
    for ticket in tickets:
        # Formatear la fecha
        date_time = ticket.event_date.date_time.astimezone(timezone('America/Bogota'))
        formatted_date = format_datetime(date_time, "d 'de' MMMM, h:mm a", locale='es')

        writer.writerow([
            ticket.person.nombre,
            ticket.person.correo,
            ticket.person.edad,
            ticket.person.genero,
            ticket.person.localidad,
            ticket.person.municipio_aledano,
            ticket.person.nivel_educativo,
            ticket.person.perfil_ocupacional,
            ticket.person.vinculacion_teatral,
            ticket.person.motivations,
            ticket.person.otras_motivaciones,
            ticket.person.medio_informacion,
            ticket.person.otros_eventos,
            'Sí' if ticket.person.comprension_datos else 'No',
            'Sí' if ticket.person.politica_datos else 'No',
            formatted_date,
            ticket.ticket_number,
            'Sí' if ticket.check_in else 'No',  # Añadir columna de asistencia
        ])

    return response
