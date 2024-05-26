from rest_framework import serializers
from .models import Function, SurveyResponse

class FunctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Function
        fields = ['date', 'available_tickets']

class SurveyResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyResponse
        fields = '__all__'