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
		'id_dni',
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
		'id_dni',
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
		'id_dni',
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
		'id_dni',
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






































def destinationAnotherCreateView(request, *args, **kwargs):
	print(request.GET)
	print(request.POST)
	form = RawDestinationForm()
	if request.method == "POST":
		form = RawDestinationForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data)
			Destination.objects.Create(**form.cleaned_data)
		else:
			print(form.errors)

	context = {
		'form' : form,
	}
	return render(request, "destinationCreate.html", context)


def destinationTestView(request, *args, **kwargs):
	obj = Destination.objects.get(id=2)
	context = {
		'objeto' : obj,
	}
	return render(request, "destination.html", context)

def destinationShowView(request, myID):
	obj = get_object_or_404( Destination, id = myID)
	context = {
		'objeto' : obj,
	}
	return render(request, 'destination.html', context)

def destinationCreateView(request):
	obj = Destination.objects.get(id = 3)
	form = AddForm(request.POST or None, request.FILES)
	#context = {}
	if form.is_valid():
		form.save()
		form = AddForm()
		return redirect('../../../')

	context = {
		'form': form,
	}
	return render(request, "destinationCreate.html", context)

def destinationEditView(request, myID):
	obj = Destination.objects.get(id = myID)
	form = AddForm(request.POST or None, request.FILES, instance = obj)
	#context = {}
	if form.is_valid():
		form.save()
		form = AddForm()
		return redirect('../../../')

	context = {
		'form': form,
	}
	return render(request, "destinationCreate.html", context)

def destinationDeleteView(request, myID):
	obj = get_object_or_404(Destination, id = myID)
	if request.method == 'POST':
		print("Lo borro")
		obj.delete()
		return redirect('../../../')

	context = {
		'objeto': obj,
	}
	return render(request, "destinationDelete.html", context)

def destinationListView(request):
	queryset = Destination.objects.all()
	context = {
		'objectList': queryset,
	}
	return render(request, "destinationList.html", context)
