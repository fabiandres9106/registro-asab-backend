from django.db import models
from django.utils.timezone import now
import random

class Theater(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    contacto = models.CharField(max_length=255)
    aforo = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Event(models.Model): 
    #Se está considerando separar Event y EventDate en dos modelos aparte. Event debe almacenar información general del evento y EventDate debe almacenar las fechas, hora de funcion y la cantidad de tickets disponibles
    teatro = models.ForeignKey(Theater, on_delete=models.CASCADE)
    nombre_evento = models.CharField(max_length=255, null=True, blank=True)
    produccion = models.CharField(max_length=255, null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    equipo_artistico = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_evento


class EventDate(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    pulep = models.CharField(max_length=10, null=True, blank=True)
    date_time = models.DateTimeField()  # Usar DateTimeField para fecha y hora
    available_tickets = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.available_tickets = self.event.teatro.aforo
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.event.teatro.nombre} - {self.date_time.strftime('%Y-%m-%d %I:%M %p')}"
    
    def tickets_not_reserved(self):
        reserved_tickets = Ticket.objects.filter(event_date=self).count()
        return self.available_tickets -  reserved_tickets


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    correo = models.EmailField(default='example@example.com', blank=True, null=True)
    edad = models.CharField(max_length=10, blank=True, null=True)
    genero = models.CharField(max_length=50, blank=True, null=True)
    localidad = models.CharField(max_length=50, blank=True, null=True)
    municipio_aledano = models.CharField(max_length=50, blank=True, null=True)
    nivel_educativo = models.CharField(max_length=50, blank=True, null=True)
    perfil_ocupacional = models.CharField(max_length=50, blank=True, null=True)
    vinculacion_teatral = models.CharField(max_length=50, blank=True, null=True)
    motivations = models.JSONField(blank=True, null=True)
    otras_motivaciones = models.CharField(max_length=255, blank=True, null=True)
    medio_informacion = models.CharField(max_length=50, default='Desconocido', blank=True, null=True)
    otros_eventos = models.JSONField(default=list, blank=True, null=True)
    comprension_datos = models.BooleanField(default=True)
    politica_datos = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    
class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    event_date = models.ForeignKey(EventDate, on_delete=models.SET_NULL, null=True, blank=True)
    ticket_number = models.IntegerField(unique=True, null=True, blank=True)
    check_in = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.ticket_number:
            self.ticket_number = self.generate_unique_ticket_number()
        super().save(*args, **kwargs)

    def generate_unique_ticket_number(self):
        while True:
            ticket_number = random.randint(100000, 999999)
            if not Ticket.objects.filter(ticket_number=ticket_number).exists():
                return ticket_number
    def __str__(self):
        return f"Ticket {self.ticket_number}: {self.person.nombre}"