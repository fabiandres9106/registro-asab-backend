from django.db import models

# Create your models here.
from django.db import models

class SurveyResponse(models.Model):
    nombre = models.CharField(max_length=255)
    edad = models.CharField(max_length=10)
    genero = models.CharField(max_length=50)
    localidad = models.CharField(max_length=50)
    motivations = models.JSONField()  # Usar JSONField para almacenar las respuestas de ranking

    def __str__(self):
        return self.nombre