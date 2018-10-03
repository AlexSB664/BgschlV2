from django.shortcuts import render
from django.views import generic
from .forms import AlumnoForm
from.models import Alumno
from django.urls import reverse_lazy
from django.contrib.auth.models import Permission

# Create your views here.
def Index(request):
	return render(request,'index.html')

class SingUp(generic.FormView):
    template_name = 'alumno/singup.html'
    form_class = AlumnoForm
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        Usr = form.save()
        prm = Permission.objects.get(codename='is_alumno')
        Usr.user_permissions.add(prm)
        Alum = Alumno()
        Alum.email = Usr
        Alum.matricula = form.cleaned_data['matricula']
        Alum.nombre = form.cleaned_data['nombre']
        Alum.apellidoPaterno = form.cleaned_data['apellidoPaterno']
        Alum.apellidoMaterno = form.cleaned_data['apellidoPaterno']
        Alum.save()
        return super(SingUp,self).form_valid(form)