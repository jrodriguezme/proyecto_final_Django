from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
# from django.views.generic import (
# 	ListView,
# 	DetailView,
# 	CreateView,
# 	UpdateView,
# 	DeleteView,
# 	)
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

def Reserva(request):
	model = Reserva
	fields = [
		'reporte'
		'nommbre',
		'apellido',
		'correo',
		'telefono',
		'fecha',
		'hora',
		'numero_mesa',
		'numero_personas',
	]