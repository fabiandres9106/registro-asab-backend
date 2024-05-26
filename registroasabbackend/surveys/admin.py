from django.contrib import admin
from .models import Function, SurveyResponse

class SurveyResponseAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'nombre', 'correo', 'edad', 'genero', 'localidad', 'municipio_aledano',
        'nivel_educativo', 'perfil_ocupacional', 'vinculacion_teatral', 'motivations', 'otras_motivaciones',
        'medio_informacion', 'otros_eventos', 'comprension_datos', 'politica_datos',
        'created_at', 'ticket_number', 'function'
    )
    list_filter = ('localidad', 'nivel_educativo', 'perfil_ocupacional', 'genero', 'function')
    search_fields = ('nombre', 'correo', 'ticket_number')
    readonly_fields = ('created_at', 'ticket_number')

class FunctionAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'available_tickets')
    list_filter = ('date',)
    search_fields = ('date',)

admin.site.register(Function, FunctionAdmin)
admin.site.register(SurveyResponse, SurveyResponseAdmin)