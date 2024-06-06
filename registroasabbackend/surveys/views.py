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
