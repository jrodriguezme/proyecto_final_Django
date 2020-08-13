from django.contrib import messages
from django.http import HttpResponse
from .utils import render_to_pdf
from django.template.loader import get_template
from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView,
	View,
	)
from .models import Reporte, Reserva
# Create your views here.

def Reporte(request):
	model = Reporte
	fields = [
		'fecha',
		'hora',
		'cliente',
		'comanda',
		'met_depago',
		'descuento',
		'total_pagar',
	]


def reserva(request):
	return render(request,'reservation.html')

class agregar(CreateView):
	model = Reserva
	fields = [
		'num_reserva',
		'nombre',
		'apellido',
		'correo', 
		'telefono',
		'fecha', 
		'hora', 
		'numero_mesa', 
		'numero_personas',
	]

class detalles(DetailView):
	model=Reserva

class listar(ListView):
	model=Reserva 

def modificar2(request):
	object_list=Reserva.objects.all()
	return render(request,'reporte/reserva_modificar.html',{'object_list':object_list})

class modificar(UpdateView):
	model = Reserva
	fields = [
		'nombre',
		'apellido',
		'correo', 
		'telefono',
		'fecha', 
		'hora', 
		'numero_mesa', 
		'numero_personas',
	]
	template_name_suffix = '_update_form'

class eliminar(DeleteView):
	model = Reserva
	success_url = reverse_lazy('reporte:listar_reserva')

def eliminar2(request):
	model = Reserva
	object_list = Reserva.objects.all()
	success_url = reverse_lazy('reporte:listar_reserva')
	return render(request,'reporte/reserva_eliminar.html',{'object_list':object_list})

class PDFReserva(View):
    def get(self, request, *args, **kwargs):
        template = get_template('pdf/pdf_reserva.html')
        html = template.render()
        queryset = Reserva.objects.all()
        context = {
            'object_list': queryset,
            'today': datetime.now(),
        }

        html = template.render(context)
        pdf = render_to_pdf('pdf/pdf_reserva.html', context)
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