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
    queryset = EventDate.objects.all()
    serializer_class = EventDateSerializer

class PersonListView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class TicketListView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class UpdateAttendanceView(generics.UpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        attended = request.data.get('attended', False)
        instance.attended = attended
        instance.save()

        if attended:
            instance.function.available_tickets -= 1
        else:
            instance.function.available_tickets += 1

        instance.function.save()
        return Response({'status': 'attendance updated'}, status=status.HTTP_200_OK)