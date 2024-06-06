from django.urls import path
from registroasabbackend.consumers import TicketConsumer

websocket_urlpatterns = [
    path('ws/tickets/', TicketConsumer.as_asgi()),
]