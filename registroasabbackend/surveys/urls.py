from django.urls import path
from .views import EventListView, EventDateListView, PersonListView, PersonDetailView, TicketListView, TicketDetailView, TicketUpdateView, hola_mundo

urlpatterns = [
    path('hola/', hola_mundo),
    path('api/events/', EventListView.as_view(), name='event-list'),
    path('api/events/<int:event_id>/event_dates', EventDateListView.as_view(), name='event_date_list'),
    path('api/events/<int:event_date>/tickets', TicketListView.as_view(), name='ticket-list'),
    path('api/events/<int:event_date>/tickets/<int:pk>', TicketDetailView.as_view(), name='ticket_detail'),
    path('api/ticket/<int:pk>/update', TicketUpdateView.as_view(), name='ticket-update'),
    path('api/person/<int:pk>', PersonDetailView.as_view(), name = 'person_detail'),
    path('api/persons/', PersonListView.as_view(), name='person-list'),
    # Otras rutas...
]