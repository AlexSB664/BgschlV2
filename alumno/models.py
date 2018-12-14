from django.db import models
from administrador.models import User
from empresa.models import Oferta
from datetime import datetime 
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Escolaridad(models.Model):
	nombre = models.CharField(unique=True,max_length=50)

	def __str__(self):
		return self.nombre

class Carrera(models.Model):
	nombre = models.CharField(unique=True,max_length=50)

	def __str__(self):
		return self.nombre

class Alumno(models.Model):
	email = models.OneToOneField(User, on_delete=models.CASCADE)
	matricula = models.CharField(max_length=50,null=True)
	escuela = models.CharField(max_length=65, null=True)
	semestre = models.IntegerField(null=True)
	egresado = models.BooleanField(default=False)
	carrera = models.ForeignKey(Carrera,on_delete=models.CASCADE,blank=True, null=True, related_name="carreraActual")
	
	is_active = models.BooleanField(
		default=False,
		help_text=_(
			'seleccionar cuando el alumno sea verificado con sus documentos.'
			'deseleccionar si el alumno no esta comprobado como un estudiante'
			),
		)

	def __str__(self):
		return self.email.nombre

	class Meta:
		permissions = (
			('is_alumno', 'Is_Alumno'),
			)
		
class Persona(models.Model):
	email = models.OneToOneField(User,on_delete=models.CASCADE)
	escolaridad = models.ForeignKey(Escolaridad,on_delete=models.CASCADE,blank=True, null=True, related_name="ultimaEscolaridad")
	experiencia = models.TextField(default="sin experiencia previa")

	def __str__(self):
		return self.email.nombre

class Solicitud(models.Model):
	oferta=models.ForeignKey(Oferta,on_delete=models.CASCADE,blank=True, null=True, related_name="solicitud")
	fecha = models.DateTimeField(default=datetime.now, blank=True)
	usuario = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True, related_name="solicitante")

	def __str__(self):
		return str(self.id+self.oferta+self.usuario+self.fecha)