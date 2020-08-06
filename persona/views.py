from django.contrib import messages
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
		'cargo',
		'id_trabajo',		
		'dni',
		'edad',
		'sexo',
		'telefono',
		'direc',
		'correo',
		'cap_esp',
		'imagen',
		'password',
	]

class PersonalUpdateView(UpdateView):
	model = Personal
	fields = [
		'nombre',
		'apellido',
		'cargo',
		'id_trabajo',		
		'dni',
		'edad',
		'sexo',
		'telefono',
		'direc',
		'correo',
		'cap_esp',
		'imagen',
		'password',
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
		'password',
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


###############################################################
def Bartender(request):
	return render(request, 'usuario/indexBartender.html')

def CRegistrado(request):
	return render(request, 'usuario/indexCRegistrado.html')

def Cajero(request):
	return render(request, 'usuario/indexCajero.html')

def JAlmacen(request):
	return	render(request, 'usuario/indexJAlmacen.html')

def Mozo(request):
	return render(request, 'usuario/indexMozo.html')	

def JCocina(request):
	return render(request, 'usuario/indexJCocina.html')	
 
def Administrador(request):
	return render(request, 'usuario/indexAdministrador.html')	

def loginExtra(request):
	if request.method == 'POST':
		id_trabajo = request.POST['id_user']
		dni 	= request.POST['username']
		password= request.POST['password']

		#usuario = Usuario.objects.get(username=dni, password=password, id_user=id_user)		
		#usuario = Usuario.authenticate(username=dni, password=password, id_user=id_user)		
		try:
		    usuario = Personal.objects.get(username=dni, password=password, id_user=id_trabajo)
		except Personal.DoesNotExist:
			usuario = None


		if usuario is not None:
			if id_user == '987':
				return redirect('JAlmacen')

			elif id_user == '990':
				return redirect('Administrador')
			
			elif id_user == '988':
				return redirect('JCocina')

			elif id_user == '222':
				return redirect('CRegistrado')
			
			elif id_user == '654':
				return redirect('Mozo')	

			elif id_user == '321':
				return redirect('Bartender')	

			elif id_user == '111':
				return redirect('Cajero')
			
			else:
				messages.info(request, 'Algùn dato es incorrecto. Vuelva a intentarlo.')
				return redirect('loginExtra')
		else:
			messages.info(request, 'Datos erroneos')
			return redirect('loginExtra')
	else:
		return render(request,'loginExtra.html')		


def registerExtra(request):
	return render(request, 'registerExtra.html')