from django.contrib import admin
from .models import Alumno, Escolaridad,Carrera, Persona,Solicitud
# Register your models here.
admin.site.register(Alumno)
admin.site.register(Escolaridad)
admin.site.register(Carrera)
admin.site.register(Persona)