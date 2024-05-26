from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponseBadRequest
from .models import Function, SurveyResponse
from .serializers import FunctionSerializer, SurveyResponseSerializer

class FunctionList(generics.ListAPIView):
    queryset = Function.objects.filter(available_tickets__gt=0)
    serializer_class = FunctionSerializer

class SurveyResponseCreate(generics.CreateAPIView):
    queryset = SurveyResponse.objects.all()
    serializer_class = SurveyResponseSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        function_date = data.get('function_date')
        function = Function.objects.filter(date=function_date).first()
        
        if not function:
            return HttpResponseBadRequest("Invalid function date.")
        if function.available_tickets <= 0:
            return JsonResponse({'message': 'No tickets available for the selected date.'}, status=400)
        
        response = SurveyResponse(
            nombre=data.get('nombre'),
            correo=data.get('correo', 'example@example.com'),
            edad=data.get('edad', ''),
            genero=data.get('genero', ''),
            localidad=data.get('localidad', ''),
            nivel_educativo=data.get('nivel_educativo', ''),
            perfil_ocupacional=data.get('perfil_ocupacional', ''),
            vinculacion_teatral=data.get('vinculacion_teatral', ''),
            motivations=data.get('motivations', {}),
            medio_informacion=data.get('medio_informacion', 'Desconocido'),
            otros_eventos=data.get('otros_eventos', []),
            comprension_datos=data.get('comprension_datos', False) == ["true"],
            politica_datos=data.get('aceptacion_politica', False) == ["true"],
            function=function
        )
        response.save()
        function.available_tickets -= 1
        function.save()
        
        return JsonResponse({'message': 'Response saved successfully!', 'ticket_number': response.ticket_number}, status=201)

class SurveyResponseList(generics.ListAPIView):
    queryset = SurveyResponse.objects.all()
    serializer_class = SurveyResponseSerializer