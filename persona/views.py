from django.conf import settings 
from django.contrib import messages
from django.http import HttpResponse
from datetime import datetime
from django.template.loader import get_template
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView,
	View,
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
		'password',
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

def gracias(email):
	send_mail('¡Hola, desde Sumaq Mikhuy Wasi!',
	'!Bienvenid@ a Sumaq Mikhuy Wasi!, Agradecemos tu confianza, estamos a su servicio.',
	'sumaqmikhuywasi@gmail.com',['carat24718@brosj.net'], fail_silently=False)

	# 	send_mail(subject, message, from_email, to_list, fail_silently=True)
	# 	subject = '!Bienvenid@ a Sumaq Mikhuy Wasi!'
	# 	message = '!Bienvenid@ a Sumaq Mikhuy Wasi!, Gracias por su registro y adquisición en nuestro restaurante. Agradecemos tu confianza, estamos a su servicio.'
	# 	from_email = settings.EMAIL_HOST_USER
	# 	to_list = [email]
	# 	send_mail(subject, message, from_email, to_list, fail_silently=True)
	return render(request, "send/gracias.html")



class PDFPersonal(View):
    def get(self, request, *args, **kwargs):
    	template = get_template('pdf/pdf_personal.html')
    	html = template.render()
    	queryset = Personal.objects.all()
    	context = {
    		'object_list': queryset,
    		'today': datetime.now(),
    	}

    	html = template.render(context)
    	pdf = render_to_pdf('pdf/pdf_personal.html', context)
    	if pdf:
    		response = HttpResponse(pdf, content_type='application/pdf')
    		filename = "Personal_%s.pdf" %("123456789")
    		content = "inline; filename=%s" %(filename)
    		download = request.GET.get("download")
    		if download:
    			content = "attachment; filename=%s"%(filename)
    		response ['Content-Disposition']= content	
    		return response
    	return HttpResponse("Not found")

class PDFCliente(View):
    def get(self, request, *args, **kwargs):
        template = get_template('pdf/pdf_cliente.html')
        html = template.render()
        queryset = Cliente.objects.all()
        context = {
            'object_list': queryset,
            'today': datetime.now(),
        }

        html = template.render(context)
        pdf = render_to_pdf('pdf/pdf_cliente.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Cliente_%s.pdf" %("123456789")
            content = "inline; filename=%s" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename=%s"%(filename)
            response ['Content-Disposition']= content   
            return response
        return HttpResponse("Not found")

class PDFProveedor(View):
    def get(self, request, *args, **kwargs):
        template = get_template('pdf/pdf_proveedor.html')
        html = template.render()
        queryset = Proveedor.objects.all()
        context = {
            'object_list': queryset,
            'today': datetime.now(),
        }

        html = template.render(context)
        pdf = render_to_pdf('pdf/pdf_proveedor.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Proveedor_%s.pdf" %("123456789")
            content = "inline; filename=%s" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename=%s"%(filename)
            response ['Content-Disposition']= content   
            return response
        return HttpResponse("Not found")
