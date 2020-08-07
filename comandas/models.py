from django.db import models
import datetime
from django.utils import timezone
from django.apps import apps
# Create your models here.
# genero = (
#        ('femenino','FEMENINO'),
#        ('masculino', 'MASCULINO'),
#        ('otro','Prefiero no decirlo'),
# )
def hora():
      hour = timezone.now()
      formatedHour = hour.strftime("%H:%M:%S")
      return formatedHour
def numero():
	numero=Formato.objects.count
class Formato(models.Model):
	numero_comanda		= numero
	hora_marca 			= models.CharField(max_length=50, default=hora)
	fecha_hoy			= datetime.date.today()
	numero_mesa			= models.IntegerField()
	numero_comensales	= models.IntegerField()
	id_camarero			= models.CharField(max_length=100)
	id_platos			= models.CharField(max_length=100)

