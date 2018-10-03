from django.db import models
from administrador.models import User
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Alumno(models.Model):
	matricula=models.CharField(max_length=30)
	nombre=models.CharField(max_length=65)
	apellidoPaterno = models.CharField(max_length = 65)
	apellidoMaterno = models.CharField(max_length = 65, null = True)
	email = models.OneToOneField(User, on_delete=models.CASCADE)
	is_active = models.BooleanField(
		default=False,
		help_text=_(
			'seleccionar cuando el alumno sea verificado con sus documentos.'
			'deseleccionar si el alumno no esta comprobado como un estudiante'
			),
		)

	def __str__(self):
		return self.nombre

	class Meta:
		permissions = (
			('is_alumno', 'Is_Alumno'),
			)