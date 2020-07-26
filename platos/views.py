from django.shortcuts import render
from .models import Platos
from django.urls import reverse_lazy
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

class listar(ListView):
	model=Platos

def modificar2(request):
	object_list=Platos.objects.all()
	return render(request,'platos/platos_modificar.html',{'object_list':object_list})

class modificar(UpdateView):
	model = Platos
	fields = [
		'nombre',
		'ciudad',
		'descripcion',
		'imagen',
		'portada',
		'oferta',
	]
	template_name_suffix = '_update_form'

class eliminar(DeleteView):
	model = Platos
	success_url = reverse_lazy('platos:listar_platos')