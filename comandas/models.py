from django.db import models
import datetime
from django.utils import timezone
from django.urls import reverse
# Create your models here.
from persona.models import Personal
from platos.models import Platos

def hora():
	hour = timezone.now()
	formatedHour = hour.strftime("%H:%M:%S")
	return formatedHour

def numero():
	numero=Formato.objects.count()
	return numero+1

class Pedido(models.Model):
	platos=models.ForeignKey(Platos,on_delete=models.DO_NOTHING) 
	Num_platos=models.IntegerField(default=0);

class Formato(models.Model):
	numero_comanda		= models.IntegerField(default=numero)
	hora_marca 			= models.CharField(max_length=50, default=hora)
	fecha_hoy			= models.CharField(max_length=50,default=datetime.date.today())
	numero_mesa			= models.IntegerField(default=0)
	numero_comensales	= models.IntegerField(default=0)
	#id_camarero			= models.CharField(max_length=100)
	id_camarero			= models.ForeignKey(Personal,on_delete=models.DO_NOTHING,related_name='camarero',null=False,blank=False)
	id_pedido			= models.ForeignKey(Platos,on_delete=models.DO_NOTHING)

	def get_absolute_url(self):
		return reverse('comandas:detalles_comandas', kwargs = {'pk': self.id})

