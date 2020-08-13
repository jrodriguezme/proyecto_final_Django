from django.db import models
import datetime
from django.utils import timezone
from django.urls import reverse
# Create your models here.
from persona.models import Personal
from platos.models import Platos

def hora():
	hour 				= timezone.now()
	formatedHour 		= hour.strftime("%H:%M:%S")
	return formatedHour

def numero():
	numero 				= Formato.objects.count()
	return numero+1


class Formato(models.Model):
	numero_comanda		= models.IntegerField(default=numero,null=True)
	hora_marca 			= models.CharField(max_length=50, default=hora,null=True)
	fecha_hoy			= models.CharField(max_length=50,default=datetime.date.today(),null=True,blank=True)
	numero_mesa			= models.IntegerField(default=0,null=True,blank=True)
	numero_comensales	= models.IntegerField(default=0,null=True,blank=True)
	id_camarero			= models.ForeignKey(Personal,on_delete=models.DO_NOTHING,related_name='camarero',default=None,null=True,blank=True)
	#pedido_id			= models.ForeignKey(Platos,on_delete=models.DO_NOTHING)

	def get_absolute_url(self):
		return reverse('comandas:detalles_comandas', kwargs = {'pk': self.id})

class Pedido(models.Model):
	codigo				= models.IntegerField(default=numero,null=True,blank=True)
	platos 				= models.ForeignKey(Platos,on_delete=models.DO_NOTHING,default=None,null=True,blank=True) 
	num_platos			= models.IntegerField(default=0,null=True,blank=True)
	vincu 				= models.ForeignKey(Formato,on_delete=models.DO_NOTHING,default=None,null=True,blank=True)
	def __str__(self):
		return self.platos
	def get_absolute_url(self):
		return reverse('comandas:detalles_comandas', kwargs = {'pk': self.id})