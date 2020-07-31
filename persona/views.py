from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView,
	)
from .models import Personal, Cliente, Proveedor
# Create your views here.

class PersonalDetailView(DetailView):
	model = Personal

class PersonalListView(ListView):
	model = Personal
	#queryset = Personal.objects.filter(edad=44)

class PersonalCreateView(CreateView):
	model = Personal
	fields = [
		'nombre',
		'apellido',
		'id_trabajo',
		'dni',
		'edad',
		'sexo',
		'telefono',
		'direc',
		'correo',
		'cap_esp',
	]

class PersonalUpdateView(UpdateView):
	model = Personal
	fields = [
		'nombre',
		'apellido',
		'id_trabajo',
		'dni',
		'edad',
		'sexo',
		'telefono',
		'direc',
		'correo',
		'cap_esp',
	]
	template_name_suffix = '_update_form'


class PersonalDeleteView(DeleteView):
	model = Personal
	success_url = reverse_lazy('persona:personal-list')


############################################

class ClienteDetailView(DetailView):
	model = Cliente

class ClienteListView(ListView):
	model = Cliente

class ClienteCreateView(CreateView):
	model = Cliente
	fields = [
		'nombre',
		'apellido',
		'id_cliente',
		'dni',
		'edad',
		'sexo',
		'direc',
		'vip',
		'especif_vip',
	]

class ClienteUpdateView(UpdateView):
	model = Cliente
	fields = [
		'nombre',
		'apellido',
		'id_cliente',
		'dni',
		'edad',
		'sexo',
		'direc',
		'vip',
		'especif_vip',
	]
	template_name_suffix = '_update_form'

class ClienteDeleteView(DeleteView):
	model = Cliente
	success_url = reverse_lazy('persona:cliente-list')

######################################################
class ProveedorDetailView(DetailView):
	model = Proveedor

class ProveedorListView(ListView):
	model = Proveedor

class ProveedorCreateView(CreateView):
	model = Proveedor
	fields = [
		'nombre',
		'ruc',
		'direc',
		'descripcion',
	]

class ProveedorUpdateView(UpdateView):
	model = Proveedor
	fields = [
		'nombre',
		'ruc',
		'direc',
		'descripcion',
	]
	template_name_suffix = '_update_form'


class ProveedorDeleteView(DeleteView):
	model = Proveedor
	success_url = reverse_lazy('persona:proveedor-list')


