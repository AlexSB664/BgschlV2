from django.db import models
from administrador.models import User
from datetime import datetime
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Empresa(models.Model):
	nombre = models.CharField(max_length=75,unique=True)
	RFC = models.CharField(max_length=50,unique=True)
	email = models.OneToOneField(User, on_delete=models.CASCADE)
	foto_empresa = models.ImageField(upload_to='empresas',null=True)
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

class Oferta(models.Model):
	empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, blank=True, null=True, related_name="ofertaEmpresa")
	fecha = models.DateTimeField(default=datetime.now, blank=True)
	descripcion  = models.TextField(default="contactanos para mas detalles.")
	escolaridad = models.CharField(max_length=65)
	carrera = models.CharField(max_length=65)
	egresado = models.BooleanField(default=False)
	abierta = models.BooleanField(default=True)
	foto = models.ImageField(upload_to='ofertas',null=True)

	def __str__(self):
		return str(self.id+self.empresa+self.fecha)