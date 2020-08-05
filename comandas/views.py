from django.shortcuts import render

# Create your views here.
def comanda(request):
	return render(request,'comandas.html')