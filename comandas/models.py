from django.db import models
import datetime
from django.utils import timezone
from django.urls import reverse
# Create your models here.


def hora():
	hour = timezone.now()
	formatedHour = hour.strftime("%H:%M:%S")
	return formatedHour

def numero():
	numero=Formato.objects.count()
	return numero+1

class Formato(models.Model):
	numero_comanda		= models.IntegerField(default=numero)
	hora_marca 			= models.CharField(max_length=50, default=hora)
	fecha_hoy			= models.CharField(max_length=50,default=datetime.date.today())
	numero_mesa			= models.IntegerField(default=0)
	numero_comensales	= models.IntegerField(default=0)
	id_camarero			= models.CharField(max_length=100)
	id_platos			= models.CharField(max_length=100)
	def get_absolute_url(self):
		return reverse('comandas:detalles_comandas', kwargs = {'pk': self.id})
