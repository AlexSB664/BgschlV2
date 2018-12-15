from django import forms
from administrador.forms import UserCreationForm2
from administrador.models import User
from alumno.models import Carrera

class AlumnoForm(UserCreationForm2):
	matricula= forms.CharField(label='Matricula:', widget=forms.TextInput(attrs={'class':'form-control'}))
	escuela = forms.CharField(label='Escuela de Procedencia:', widget=forms.TextInput(attrs={'class':'form-control'}))
	semestre = forms.CharField(label='Semestre:', widget=forms.TextInput(attrs={'class':'form-control'}))
	egresado = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), choices=((0,'No'),(1,'Si')),label='¿Eres egresado?:')
	choices=[(choice.pk, choice) for choice in Carrera.objects.all()]
	carrera = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), choices=choices,label='¿Que carrera estas estudiando?:')


	class Meta(UserCreationForm2.Meta):
		model = User
		fields = UserCreationForm2.Meta.fields
		widgets = {
			'email': forms.TextInput(attrs = {'class':'form-control'}),
			'password1': forms.PasswordInput(attrs = {'class' : 'form-control'}),
			'nombre': forms.PasswordInput(attrs = {'class' : 'form-control'}),
			'apellido_paterno': forms.PasswordInput(attrs = {'class' : 'form-control'}),
			'apellido_materno': forms.PasswordInput(attrs = {'class' : 'form-control'}),
			'fecha_nacimiento': forms.PasswordInput(attrs = {'class' : 'form-control'}),
			'genero': forms.PasswordInput(attrs = {'class' : 'form-control'}),
			'foto_perfil': forms.FileInput(attrs = {'class' : 'form-control'}),
		}
		labels = {
			'email' : 'Correo:',
			'password1': 'Contraseña',
			'password2': 'Confirmar Contraseña',
			'nombre' : 'Nombre:',
			'apellido_paterno' : 'Apellido Paterno:',
			'apellido_materno' : 'Apellido Materno:',
			'fecha_nacimiento' : 'Fecha de Nacimiento:',
			'genero' : 'Genero:',
			'foto_perfil' : 'Foto de Perfil:',
		}