from django.db import models
from django.urls import reverse

# Create your models here.
class Platos(models.Model):
	nombre		= models.CharField(max_length=100)
	ciudad		= models.CharField(max_length=100)
	descripcion	= models.TextField()
	imagen		= models.ImageField(upload_to='images')
	portada 	= models.BooleanField(default=False)
	oferta		= models.BooleanField(default=False)
	def get_absolute_url(self):
		return reverse('platos:detalles_plato', kwargs = {'pk': self.id})

