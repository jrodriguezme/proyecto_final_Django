from django.db import models
from django.contrib.auth.hashers import make_password
from persona.models import Personal
# Create your models here.
class Usuario(models.Model):
	id_trabajo = models.CharField(max_length=100)
	cargo = models.CharField(max_length=100)
	username = models.ForeignKey(Personal, on_delete=models.CASCADE)
	password = make_password('')
