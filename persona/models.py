from django.db import models
from django.urls import reverse
#from usuario.models import Usuario
# Create your models here.

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

	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	id_trabajo = models.IntegerField()
	cargo = models.CharField(max_length=100, choices=puesto, default='otro')
	dni = models.IntegerField()
	edad = models.IntegerField()
	sexo = models.CharField(max_length=100, choices=genero, default='otro')
	telefono = models.IntegerField()
	direc = models.CharField(max_length=100)
	correo = models.CharField(max_length=50)
	cap_esp = models.BooleanField(default=False)
	imagen = models.ImageField(upload_to='persona',default='persona/sin_imagen.jpg') 

	def get_absolute_url(self):
		return reverse('persona:personal-detail', kwargs = {'pk': self.id})


class Cliente(models.Model):

	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	id_cliente = models.IntegerField(default=222)
	dni = models.IntegerField()
	edad = models.IntegerField(default=False)
	sexo = models.CharField(max_length=100, choices=genero, default='otro')
	direc = models.CharField(max_length=100, default='No requiere delibery')
	vip = models.BooleanField(default=False)
	especif_vip = models.CharField(max_length=100, default='Ninguna')

	def get_absolute_url(self):
		return reverse('persona:cliente-detail', kwargs = {'pk': self.id})


class Proveedor(models.Model):

	nombre = models.CharField(max_length=100)
	ruc = models.IntegerField()
	direc = models.CharField(max_length=100)
	descripcion = models.TextField()

	def get_absolute_url(self):
		return reverse('persona:proveedor-detail', kwargs = {'pk': self.id})
