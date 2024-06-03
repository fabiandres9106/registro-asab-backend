from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
from django.http import JsonResponse, HttpResponseBadRequest
from .models import Event, EventDate, Person, Ticket
from .serializers import EventSerializer, EventDateSerializer, PersonSerializer, TicketSerializer
from datetime import datetime

def hola_mundo(request):
    return JsonResponse({"mensaje": "hola_mundo"})

class EventListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDateListView(generics.ListAPIView):    
    serializer_class = EventDateSerializer

    def get_queryset(self):
        event_id = self.kwargs['event_id']
        return EventDate.objects.filter(event_id=event_id)

class PersonListView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonDetailView(generics.RetrieveAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class TicketListView(generics.ListCreateAPIView):
    serializer_class = TicketSerializer

    def get_queryset(self):
        event_date = self.kwargs['event_date']
        return Ticket.objects.filter(event_date=event_date)
    
class TicketDetailView(generics.RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class TicketUpdateView(generics.UpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer