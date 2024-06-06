from django.core.mail import send_mail
from django.conf import settings

def send_confirmation_email(person, event_date):
    subject = 'Confirmación de registro'
    message = f"""
    Hola {person.nombre},

    Gracias por registrarte para asistir a nuestro evento. Aquí tienes los detalles de tu registro:

    Fecha de la función: {event_date.date_time.strftime('%d de %B, %I:%M %p')}

    Esperamos verte allí!

    Saludos,
    El equipo de organización
    """
    recipient_list = [person.correo]
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)