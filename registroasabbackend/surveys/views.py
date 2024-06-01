from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
from django.http import JsonResponse, HttpResponseBadRequest
from .models import Function, SurveyResponse
from .serializers import FunctionSerializer, SurveyResponseSerializer
from datetime import datetime

def hola_mundo(request):
    return JsonResponse({"mensaje": "hola_mundo"})

class FunctionViewSet(viewsets.ModelViewSet):
    queryset = Function.objects.all()  # Asegúrate de que aquí no se esté utilizando 'date'
    serializer_class = FunctionSerializer

class FunctionList(generics.ListAPIView):
    queryset = Function.objects.filter(available_tickets__gt=0)
    serializer_class = FunctionSerializer

class SurveyResponseCreate(generics.CreateAPIView):
    queryset = SurveyResponse.objects.all()
    serializer_class = SurveyResponseSerializer

    def create(self, request, *args, **kwargs):
        data = request.data

        function_id = data.get('function_date')
        
        try:
            function_date = Function.objects.get(id=function_id)
            print(function_date)
        except ValueError:
            return HttpResponseBadRequest("Invalid function date format. Use 'YYYY-MM-DDTHH:MM:SS' format.")

        function = function_date
        
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
            municipio_aledano=data.get('municipio_aledano', ''),
            nivel_educativo=data.get('nivel_educativo', ''),
            perfil_ocupacional=data.get('perfil_ocupacional', ''),
            vinculacion_teatral=data.get('vinculacion_teatral', ''),
            motivations=data.get('motivations', {}),
            otras_motivaciones=data.get('otras_motivaciones', ''),
            medio_informacion=data.get('medio_informacion', 'Desconocido'),
            otros_eventos=data.get('otros_eventos', []),
            comprension_datos=data.get('comprension_datos', False) == ["true"],
            politica_datos=data.get('politica_datos', False) == ["true"],
            function=function
        )
        response.save()
        function.available_tickets -= 1
        function.save()
        
        return JsonResponse({'message': 'Response saved successfully!', 'ticket_number': response.ticket_number}, status=201)

class SurveyResponseList(generics.ListAPIView):
    queryset = SurveyResponse.objects.all()
    serializer_class = SurveyResponseSerializer

class FunctionListView(generics.ListAPIView):
    queryset = Function.objects.all()
    serializer_class = FunctionSerializer

class SurveyResponseListView(generics.ListAPIView):
    serializer_class = SurveyResponseSerializer

    def get_queryset(self):
        function_id = self.kwargs['function_id']
        return SurveyResponse.objects.filter(function_id=function_id)
    
class SurveyResponseDetailView(generics.RetrieveAPIView):
    queryset = SurveyResponse.objects.all()
    serializer_class = SurveyResponseSerializer