from django.db import models

# Create your models here.
class Usuario(models.Model):
	id_user = models.CharField(max_length=100)
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
