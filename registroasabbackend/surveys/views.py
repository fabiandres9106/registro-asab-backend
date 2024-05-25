from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import SurveyResponse
import json

@csrf_exempt
def survey_response(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        response = SurveyResponse(
            nombre=data.get('nombre'),
            edad=data.get('edad'),
            genero=data.get('genero'),
            localidad=data.get('localidad'),
            motivations=data.get('motivations')
        )
        response.save()
        return JsonResponse({'message': 'Response saved successfully!'}, status=201)