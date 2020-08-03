from django.shortcuts import render
from platos.models import Platos
from persona.models import Personal

# Create your views here.

def index(request):
	platos=Platos.objects.all()
	personal=Personal.objects.all()
	numeroPersonal = Personal.objects.count()+1
	return render(request,'index.html',{'platos':platos,'personal':personal,'numeroPersonal':numeroPersonal})
def nosotros(request):
	return render(request,'about.html')

def blog(request):
	return render(request,'blog.html')

def contactanos(request):
	return render(request,'contact.html')

def menu(request):
	return render(request,'menu.html')
