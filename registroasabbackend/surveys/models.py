from django.db import models
from django.utils.timezone import now
import random

class Function(models.Model):
    date = models.DateField()
    available_tickets = models.PositiveIntegerField(default=85)

    def __str__(self):
        return f"Function on {self.date} - Tickets available: {self.available_tickets}"

class SurveyResponse(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    correo = models.EmailField(default='example@example.com', blank=True, null=True)
    edad = models.CharField(max_length=10, blank=True, null=True)
    genero = models.CharField(max_length=50, blank=True, null=True)
    localidad = models.CharField(max_length=50, blank=True, null=True)
    nivel_educativo = models.CharField(max_length=50, blank=True, null=True)
    perfil_ocupacional = models.CharField(max_length=50, blank=True, null=True)
    vinculacion_teatral = models.CharField(max_length=50, blank=True, null=True)
    motivations = models.JSONField(blank=True, null=True)
    medio_informacion = models.CharField(max_length=50, default='Desconocido', blank=True, null=True)
    otros_eventos = models.JSONField(default=list, blank=True, null=True)
    comprension_datos = models.BooleanField(default=False)  # Campo añadido anteriormente
    politica_datos = models.BooleanField(default=False)  # Nuevo campo
    created_at = models.DateTimeField(auto_now_add=True)
    ticket_number = models.IntegerField(unique=True, null=True, blank=True)
    function = models.ForeignKey(Function, on_delete=models.CASCADE, default=1)

    def save(self, *args, **kwargs):
        if not self.ticket_number:
            self.ticket_number = self.generate_unique_ticket_number()
        super().save(*args, **kwargs)

    def generate_unique_ticket_number(self):
        while True:
            ticket_number = random.randint(100000, 999999)  # Genera un número de 6 dígitos
            if not SurveyResponse.objects.filter(ticket_number=ticket_number).exists():
                return ticket_number

    def __str__(self):
        return f"Ticket {self.ticket_number}: {self.nombre}"