from django.contrib import admin
from .models import Function, SurveyResponse

class SurveyResponseAdmin(admin.ModelAdmin):
    list_display = (
        'nombre', 'correo', 'edad', 'genero', 'localidad', 
        'nivel_educativo', 'perfil_ocupacional', 'vinculacion_teatral',
        'motivations', 'medio_informacion', 'otros_eventos',
        'comprension_datos', 'politica_datos', 'ticket_number', 'function', 'created_at'
    )
    list_filter = ('function', 'medio_informacion', 'comprension_datos', 'politica_datos')
    search_fields = ('nombre', 'correo', 'ticket_number')

admin.site.register(Function)
admin.site.register(SurveyResponse, SurveyResponseAdmin)