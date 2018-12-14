from django.shortcuts import render

# Create your views here.
def demostradores(request):
	return render(request,'demostradores.html')