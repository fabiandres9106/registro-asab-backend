from django.urls import path
from .views import survey_response

urlpatterns = [
    path('api/survey/', survey_response),
]