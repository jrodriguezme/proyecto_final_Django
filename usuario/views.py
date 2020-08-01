from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import Enter
from usuario.models import Usuario

# Create your views here.
def index(request):
	return render(request, 'index.html')

def loginExtra(request):
	if request.method == 'POST':
		id_user = request.POST['id_user']
		dni = request.POST['username']
		password = request.POST['password']

		usuario = Usuario.objects.get(username=dni, password=password, id_user=id_user)		
		if usuario is not None:

			return redirect("../")
		else:
			messages.info(request, 'Datos erroneos')
			return redirect('loginExtra')
	else:
		return render(request,'loginExtra.html')		
