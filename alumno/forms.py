from django import forms
from administrador.forms import UserCreationForm
from administrador.models import User

class AlumnoForm(UserCreationForm):
	matricula= forms.CharField(label='matricula:', widget=forms.TextInput(attrs={'class':'form-control'}))
	nombre = forms.CharField(label='Nombre:', widget=forms.TextInput(attrs={'class':'form-control'}))
	apellidoPaterno = forms.CharField(label='Apellido Paterno:', widget=forms.TextInput(attrs={'class':'form-control'}))
	apellidoMaterno = forms.CharField(label='Apellido Materno:', widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta(UserCreationForm.Meta):
		model = User
		fields = UserCreationForm.Meta.fields
		widgets = {
			'email': forms.TextInput(attrs = {'class':'form-control'}),
			'password1': forms.PasswordInput(attrs = {'class' : 'form-control'}),
		}
		labels = {
			'email' : 'Correo:',
			'password1': 'Contraseña',
		}