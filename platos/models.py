from django.db import models

# Create your models here.
class Platos(models.Model):
	nombre		= models.CharField(max_length=100)
	region		= models.CharField(max_length=100)
	descripcion	= models.TextField()
	imagen		= models.ImageField(upload_to='Images')
	exclusivo 	= models.BooleanField(default=False)
	oferta		= models.BooleanField(default=False)


