from django.shortcuts import render
from platos.models import Platos
# Create your views here.

def index(request):
	platos=Platos.objects.all()
	return render(request,'index.html',{'platos':platos})
