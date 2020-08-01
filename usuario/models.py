from django.db import models

# Create your models here.
class Usuario(models.Model):
	id_user = models.IntegerField()
	username = models.IntegerField()
	password = models.CharField(max_length=100)


