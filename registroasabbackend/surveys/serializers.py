from rest_framework import serializers
from .models import Person, Ticket, Theater, Event, EventDate

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    teatro = serializers.StringRelatedField()

    class Meta:
        model = Event
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class TheaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theater
        fields = '__all__'

class EventDateSerializer(serializers.ModelSerializer):
    tickets_not_reserved = serializers.SerializerMethodField()

    class Meta:
        model = EventDate
        fields = '__all__'

    def get_tickets_not_reserved(self, obj):
        return obj.tickets_not_reserved()