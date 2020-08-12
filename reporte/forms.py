from django import forms
from .models import Reserva

class AddReserva(forms.ModelForm):
	class Meta:
		model = Destination
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

