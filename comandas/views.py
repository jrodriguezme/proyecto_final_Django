from django.shortcuts import render
from .models import Formato
from django.urls import reverse_lazy
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView,
	)
# Create your views here.
class comanda(CreateView):
	model=Formato
	model.numero_comanda=model.objects.count
	fields = [
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