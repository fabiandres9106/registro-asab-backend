from django.contrib import admin
from .models import Function, SurveyResponse
from django.utils.timezone import localtime

class SurveyResponseAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'correo', 'edad', 'genero', 'localidad', 'formatted_function_date_time')

    def formatted_function_date_time(self, obj):
        return localtime(obj.function.date_time).strftime('%Y-%m-%d %I:%M %p')
    formatted_function_date_time.short_description = 'Function Date Time'
    

class FunctionAdmin(admin.ModelAdmin):
    list_display = ('id', 'formatted_date_time', 'available_tickets')
    def formatted_date_time(self, obj):
        return localtime(obj.date_time).strftime('%Y-%m-%d %I:%M %p')
    formatted_date_time.short_description = 'Date Time'

admin.site.register(Function, FunctionAdmin)
admin.site.register(SurveyResponse, SurveyResponseAdmin)