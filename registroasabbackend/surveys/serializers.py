from rest_framework import serializers
from .models import Person, Ticket, Theater, Event, EventDate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Agregar roles al token
        token['roles'] = [group.name for group in user.groups.all()]
        token['username'] = user.username

        return token

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    teatro = serializers.StringRelatedField()
    event_dates_count = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = '__all__'

    def get_event_dates_count(self, obj):
        return obj.event_dates_count()

class TicketSerializer(serializers.ModelSerializer):
    person = PersonSerializer(read_only=True)
    event = EventSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'

class TheaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theater
        fields = '__all__'

class EventDateSerializer(serializers.ModelSerializer):
    tickets_not_reserved = serializers.SerializerMethodField()
    tickets_reserved = serializers.SerializerMethodField()
    tickets_checkin = serializers.SerializerMethodField()

    class Meta:
        model = EventDate
        fields = '__all__'

    def get_tickets_not_reserved(self, obj):
        return obj.tickets_not_reserved()
    
    def get_tickets_reserved(self, obj):
        return obj.tickets_reserved()
    
    def get_tickets_checkin(self, obj):
        return obj.tickets_checkin()