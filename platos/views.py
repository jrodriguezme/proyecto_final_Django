from django.shortcuts import render
from .models import Platos
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView,
	)
# Create your views here. 

def platos(request):
	return render(request,'platos.html')

class agregar(CreateView):
	model = Platos
	fields = [
		'nombre',
		'ciudad',
		'descripcion',
		'imagen',
		'portada',
		'oferta',
	]
class detalles(DetailView):
	model=Platos
def listar(request):
	return render(request,'listarPlato.html')

def modificar(request):
	return render(request,'modificarPlato.html')

def eliminar(request):
	return render(request,'eliminarPlato.html')