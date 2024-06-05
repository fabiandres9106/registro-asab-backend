from django.urls import path
from .views import EventListView, EventDateListView, PersonListView, PersonDetailView, TicketListView, TicketDetailView, TicketUpdateView, EventDateDetailView, hola_mundo
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CustomTokenObtainPairView  # Importa la vista personalizada

urlpatterns = [
    path('hola/', hola_mundo),
    path('api/events/', EventListView.as_view(), name='event-list'),
    path('api/tickets/', TicketListView.as_view(), name='tickets-list'),
    path('api/events/<int:event_id>/event_dates', EventDateListView.as_view(), name='event_date_list'),
    path('api/event_dates/<int:pk>', EventDateDetailView.as_view(), name='event_date_list'),
    path('api/events/<int:event_date>/tickets', TicketListView.as_view(), name='ticket-list'),
    path('api/events/<int:event_date>/tickets/<int:pk>', TicketDetailView.as_view(), name='ticket_detail'),
    path('api/ticket/<int:pk>/update', TicketUpdateView.as_view(), name='ticket-update'),
    path('api/person/<int:pk>', PersonDetailView.as_view(), name = 'person_detail'),
    path('api/persons/', PersonListView.as_view(), name='person-list'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # Usa la vista personalizada
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Otras rutas...
]