from django.db import models
from django.urls import reverse
#from usuario.models import Usuario
# Create your models here.
from platos.models import Platos
genero = (
       ('femenino','FEMENINO'),
       ('masculino', 'MASCULINO'),
       ('otro','Prefiero no decirlo'),
)
puesto = (
	('administrador','ADMINISTRADOR'),
	('jefe de cocina','JEFE DE COCINA'),
	('jefe de almacen','JEFE DE ALMACEN'),
	('recepcionista','RECEPCIONISTA'),
	('cajero','CAJERO'),
	('mesero','MESERO'),
	('bartender','BARTENDER'),
	('cocinero','COCINERO'),
	('otro','VARIOS'),
)


class Personal(models.Model):

	nombre 		= models.CharField(max_length=100)
	apellido 	= models.CharField(max_length=100)
	cargo 		= models.CharField(max_length=100, choices=puesto, default='otro')	
	id_trabajo 	= models.CharField(max_length=100)
	dni 		= models.CharField(max_length=100)
	edad 		= models.IntegerField()
	sexo 		= models.CharField(max_length=100, choices=genero, default='otro')
	telefono 	= models.IntegerField()
	direc 		= models.CharField(max_length=100)
	correo 		= models.CharField(max_length=50)
	cap_esp 	= models.BooleanField(default=False)
	imagen 		= models.ImageField(upload_to='persona',default='persona/sin_imagen.jpg') 
	password	= models.CharField(max_length=50, default='sumaq123')

	def __str__(self):
		datos=self.nombre+" "+self.apellido
		return datos

	# def id_trabajo(self):
	# 	if self.cargo == 'administrador':
	# 		return '2002'
	# 	elif self.cargo == 'jefe de cocina':
	# 		return '998'
	# 	elif self.cargo == 'jefe de almacen':
	# 		return '987'
	# 	elif self.cargo == 'cajero':
	# 		return '111'								
	# 	elif self.cargo == 'mesero':
	# 		return '654'
	# 	elif self.cargo == 'bartender':
	# 		return '321'						
	# 	else:
	# 		return '1000'

	def get_absolute_url(self):
		return reverse('persona:personal-detail', kwargs = {'pk': self.id})
	


class Cliente(models.Model):

	nombre 		= models.CharField(max_length=100)
	apellido 	= models.CharField(max_length=100)
	id_trabajo 	= models.CharField(max_length=100, default=222)
	dni 		= models.IntegerField()
	edad 		= models.IntegerField(default=False)
	sexo 		= models.CharField(max_length=100, choices=genero, default='otro')
	direc 		= models.CharField(max_length=100, default='No requiere delibery')
	vip 		= models.BooleanField(default=False)
	especif_vip = models.CharField(max_length=100, default='Ninguna')
	password 	= models.CharField(max_length=50)	
	comandas 	= models.ManyToManyField(Platos, through='Comanda')	
	
	def  id_cliente(self):
		return '222'

	def get_absolute_url(self):
		return reverse('persona:cliente-detail', kwargs = {'pk': self.id})


class Proveedor(models.Model):
	nombre 		= models.CharField(max_length=100)
	ruc			= models.IntegerField()
	direc 		= models.CharField(max_length=100)
	descripcion = models.TextField()

	def __str__(self):
		datos=self.nombre
		return datos

	def get_absolute_url(self):
		return reverse('persona:proveedor-detail', kwargs = {'pk': self.id})


class Comanda(models.Model):
	customer = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	dish = models.ForeignKey(Platos, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)