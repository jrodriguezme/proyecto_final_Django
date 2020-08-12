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
	#	'id_trabajo',		
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
	#	'id_trabajo',		
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
	#	'id_trabajo',
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
	#	'id_trabajo',
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


# class Comanda(models.Model):
# 	model = Comanda
# 	fields = [
# 		'customer',
# 		'dish',
# 		'quantity',
# 	]

###############################################################

def loginExtra(request):
	if request.method == 'POST':
		id_trabajo = request.POST['id_user']
		dni 	= request.POST['username']
		password= request.POST['password']

		if id_trabajo == '222':
			try:
		 		person2 = Cliente.objects.get(dni=dni, password=password, id_trabajo=id_trabajo)			
			except Cliente.DoesNotExist:
 	 			person2 = None
		else:
			try:
		 		person = Personal.objects.get(dni=dni, password=password, id_trabajo=id_trabajo)
			except Personal.DoesNotExist: 
 		 		person = None 			

		if person2 is not None:
 			if id_trabajo =='222':
 				return render(request, 'usuario/indexCRegistrado.html')
 			else:
 				messages.info(request, 'Algún dato es incorrecto. Vuelva a intentarlo.')
 				return redirect('loginExtra')
		else:
 			messages.info(request, 'Datos erroneos')
 			return redirect('loginExtra')


		if person is not None:
			if id_trabajo== '987':
				return render(request, 'usuario/indexJAlmacen.html')

			elif id_trabajo == '990':
				return render(request, 'usuario/indexAdministrador.html')
			
			elif id_trabajo == '988':
				return render(request, 'usuario/indexJCocina.html')
			
			elif id_trabajo == '654':
				return render(request,'usuario/indexMozo.html')	

			elif id_trabajo == '321':
				return render(request, 'usuario/indexBartender.html')	

			elif id_trabajo == '111':
				return render(request, 'usuario/indexCajero.html')
			
			else:
				messages.info(request, 'Algún dato es incorrecto. Vuelva a intentarlo.')
				return redirect('loginExtra')
		else:
			messages.info(request, 'Datos erroneos')
			return redirect('loginExtra')
	else:
		return render(request,'loginExtra.html')		


def registerExtra(request):
	return render(request, 'registerExtra.html')