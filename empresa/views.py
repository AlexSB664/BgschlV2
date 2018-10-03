from django.shortcuts import render

# Create your views here.
class SingUp(generic.FormView):
    template_name = 'alumno/singup.html'
    form_class = AlumnoForm
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        Usr = form.save()
        prm = Permission.objects.get(codename='is_alumno')
        Usr.user_permissions.add(prm)
        Alum = Alumno()
        Alum.name = Usr
        Alum.apellidos = form.cleaned_data['apellidos']
        Alum.email = form.cleaned_data['email']
        Alum.save()
        return super(SingUp,self).form_valid(form)