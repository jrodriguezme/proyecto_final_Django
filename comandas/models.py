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
num_personas = (
	(1, '1'),
	(2, '2'),
	(3, '3'),
	(4, '4'),
	(5, '5'),
	('mas de 5', 'Mas de 5'),
)

def contador():
	Formato=apps.get_model(app_label='comandas',model_name='Formato')
	return Formato.objects.count()
	
class Formato(models.Model):
	#numero_comanda		= models.IntegerField(default=contador())
	fecha_hoy			= datetime.date.today()
	numero_mesa			= models.IntegerField()
	numero_comensales	= models.IntegerField()
	id_camarero			= models.CharField(max_length=100)
	id_platos			= models.CharField(max_length=100)
