from django.db import models
from administrador.models import User
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Empresa(models.Model):
	nombre = models.CharField(max_length=75)
	representante = models.CharField(max_length=105)
	email = models.OneToOneField(User, on_delete=models.CASCADE)
	sector = models.CharField(max_length=75,null=True)
	is_active = models.BooleanField(
		default=False,
		help_text=_(
			'seleccionar cuando la empresa sea verificado con sus documentos.'
			'deseleccionar si la empresa no esta comprobado'
			),
		)

	def __str__(self):
		return self.nombre

	class Meta:
		permissions = (
			('is_empresa', 'Is_Empresa'),
			)