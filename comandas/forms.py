from django import forms
from .models import Formato,Pedido

from django.forms import ModelForm
from django.forms import formset_factory


CHOICES=[
	(1,'choice 1'),
	(2,'choice 2'),
]
class addForm(forms.ModelForm):
	class Meta:
		model=Formato
		fields = [
			'numero_comanda',
			'hora_marca',
			'fecha_hoy',
			'numero_mesa',
			'numero_comensales',
			'id_camarero',
		]
		labels={
			'numero_comanda':'numero de comanda',
			'hora_marca':'Hora',
			'fecha_hoy':'fecha',
			'numero_mesa':'mesa',
			'numero_comensales':'personas',
			'id_camarero':'codigo de personal',
		}
		widgets={
			'numero_comanda':forms.NumberInput(attrs={'placeholder':'numero de pedido','disabled':'disabled'}),
			'hora_marca':forms.TextInput(attrs={'placeholder':'hora de pedido','disabled':'disabled'}),
			'fecha_hoy':forms.TextInput(attrs={'placeholder':'fecha','disabled':'disabled'}),
			'numero_mesa':forms.NumberInput(attrs={'placeholder':'numero de mesa','min':"0"}),
			'numero_comensales':forms.NumberInput(attrs={'placeholder':'numero de comensales','min':"0"}),
			

		}

class pedidoForm(forms.ModelForm):
	class Meta:
		model=Pedido
		fields=[
			'platos',
			'num_platos',
		]
		labels={
			'platos':"Plato pedido",
			'num_platos':'numero de platos'
		}
		widgets={
			
			'num_platos':forms.NumberInput(attrs={'placeholder':'numero de comensales','min':"0"})
		}
		