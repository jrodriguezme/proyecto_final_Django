from django.db import models
import datetime
from django.utils import timezone
from django.urls import reverse
# Create your models here.
from persona.models import Cliente, Comanda


met_pago = (
	('tarjeta','TARJETA'),
	('efectivo','EFECTIVO'),
)

desc = (
	('vip','CLIENTE VIP: 40%'),
	('golden', 'TARJETA DORADA: 25%'),
	('festivo','DIA FESTIVO: 15%'),
	('cumpleaños','TU CUMPLEAÑOS: 20%'),
	('aniversario','ANIVERSARIO DE CASA: 50%'),
	('ninguno','ninguno'),
)

def hora():
	hour 				= timezone.now()
	formatedHour 		= hour.strftime("%H:%M:%S")
	return formatedHour

def numero():
	numero 				= Reserva.objects.count()
	return numero+1

class Reporte(models.Model):
	fecha 	= datetime.date.today()
	hora 	= models.DateField()
	cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
	comanda = models.OneToOneField(Comanda, on_delete=models.CASCADE)
	cuenta 	= models. IntegerField()
	met_de_pago = models.CharField(max_length=100, choices=met_pago, default='efectivo')
	descuento 	= models.CharField(max_length=100, choices=desc, default='ninguno')
	total_pagar = models.IntegerField()


class Reserva(models.Model):
#	reporte = models.OneToOneField('Reporte', on_delete=models.CASCADE, blank=True)
	num_reserva = models.IntegerField(default=numero)
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	correo =  models.EmailField(max_length=100)
	telefono = models.IntegerField()
	fecha = models.DateField()
	hora = models.TimeField()
	numero_mesa = models.IntegerField()
	numero_personas = models.IntegerField(default=1)

	def get_absolute_url(self):
		return reverse('reporte:detalles_reserva', kwargs = {'pk': self.id})
