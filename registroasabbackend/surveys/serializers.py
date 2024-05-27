from rest_framework import serializers
from .models import Function, SurveyResponse

class FunctionSerializer(serializers.ModelSerializer):
    date_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M')

    class Meta:
        model = Function
        fields = ['id', 'date_time', 'available_tickets']

class SurveyResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyResponse
        fields = [
            'id', 'nombre', 'correo', 'edad', 'genero', 'localidad', 'municipio_aledano',
            'nivel_educativo', 'perfil_ocupacional', 'vinculacion_teatral', 'motivations',
            'medio_informacion', 'otros_eventos', 'comprension_datos', 'politica_datos',
            'created_at', 'ticket_number', 'function'
        ]