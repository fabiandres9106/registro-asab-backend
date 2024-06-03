from django.contrib import admin
from .models import Person, Theater, Ticket, Event, EventDate
from django.utils.timezone import localtime


class PersonAdmin(admin.ModelAdmin):
    pass

class EventAdmin(admin.ModelAdmin):
    pass

class TheaterAdmin(admin.ModelAdmin):
    pass

class TicketAdmin(admin.ModelAdmin):
    pass

class EventDateAdmin(admin.ModelAdmin):
    pass

admin.site.register(Event, EventAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Theater, TheaterAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(EventDate, EventDateAdmin)