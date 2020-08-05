from django.db import models
import datetime
# Create your models here.

class Formato(models.Model):
	numero_comanda		= Formato.objects.count()+1
	fecha_hoy			= models.DateField(default = date.today)
	numero_mesa			= models.IntegerField()
	numero_comensales	= models.IntegerField()
	id_camarero			= models.CharField(max_length=100)
	id_platos			= ArrayField(ArrayField(models.IntegerField(),default=[]))
