from django.urls import path
from .views import FunctionList, SurveyResponseCreate, FunctionListView, SurveyResponseListView, SurveyResponseDetailView, hola_mundo

urlpatterns = [
    path('hola/', hola_mundo),
    path('api/survey/', SurveyResponseCreate.as_view(), name='survey-response-create'),
    path('api/functions/', FunctionList.as_view(), name='function-list'),
    path('api/functions/<int:function_id>/responses/', SurveyResponseListView.as_view(), name='surveyresponse-list'),
    path('api/responses/<int:pk>/', SurveyResponseDetailView.as_view(), name='surveyresponse-detail')
    # Otras rutas...
]