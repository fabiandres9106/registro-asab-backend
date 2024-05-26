from django.urls import path
from .views import FunctionList, SurveyResponseCreate

urlpatterns = [
    path('api/functions/', FunctionList.as_view(), name='function-list'),
    path('api/survey/', SurveyResponseCreate.as_view(), name='survey-response-create'),
    # Otras rutas...
]