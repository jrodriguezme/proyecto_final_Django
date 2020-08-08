from django.shortcuts import render
from .models import Formato
from persona.models import Personal 
from django.urls import reverse_lazy
from django.urls import reverse
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView,
	)
# Create your views here.
def comandas(request):
	personas=Personal.objects.all()
	return render(request,'comandas/comandas.html',{'personas':personas})

class agregar(CreateView):
	model=Formato
	fields = [
		'hora_marca',
		'fecha_hoy',
		'numero_comanda',
		'numero_mesa',
		'numero_comensales',
		'id_camarero',
		'id_platos',
	]

class detalles(DetailView):
	model=Formato

class listar(ListView):
	model=Formato

def modificar2(request):
	object_list=Formato.objects.all()
	return render(request,'comandas/formato_modificar.html',{'object_list':object_list})

class modificar(UpdateView):
	model = Formato
	fields = [
		'hora_marca',
		'fecha_hoy',
		'numero_comanda',
		'numero_mesa',
		'numero_comensales',
		'id_camarero',
		'id_platos',
	]
	template_name_suffix = '_update_form'

class eliminar(DeleteView):
	model = Formato
	success_url = reverse_lazy('comandas:listar_comandas')

def eliminar2(request):
	model = Formato
	object_list=Formato.objects.all()
	success_url = reverse_lazy('comandas:listar_comandas')
	return render(request,'comandas/formato_eliminar.html',{'object_list':object_list})