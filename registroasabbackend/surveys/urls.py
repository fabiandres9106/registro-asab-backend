from django.urls import path
from .views import EventListView, EventDateListView, PersonListView, TicketListView, UpdateAttendanceView, hola_mundo

urlpatterns = [
    path('hola/', hola_mundo),
    path('api/events/', EventListView.as_view(), name='event-list'),
    path('api/event_dates/', EventDateListView.as_view(), name='event_date_list'),
    path('api/persons/', PersonListView.as_view(), name='person-list'),
    path('api/tickets/', TicketListView.as_view(), name='ticket-list'),
    path('api/tickets/<int:pk>/attendance/', UpdateAttendanceView.as_view(), name='update-attendance'),
    # Otras rutas...
]