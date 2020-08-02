from django.shortcuts import render, redirect
from django.contrib import messages
from usuario.models import Usuario


# Create your views here.
def Bartender(request):
	return render(request, 'indexBartender.html')

def CRegistrado(request):
	return render(request, 'indexCRegistrado.html')

def Hostess(request):
	return render(request, 'indexHostess.html')

def JAlmacen(request):
	return	render(request, 'indexJAlmacen.html')

def Mozo(request):
	return render(request, 'indexMozo.html')	

def loginExtra(request):
	if request.method == 'POST':
		id_user = request.POST['id_user']
		dni 	= request.POST['username']
		password= request.POST['password']

		#usuario = Usuario.objects.get(username=dni, password=password, id_user=id_user)		
		#usuario = Usuario.authenticate(username=dni, password=password, id_user=id_user)		
		try:
		    usuario = Usuario.objects.get(username=dni, password=password, id_user=id_user)
		except Usuario.DoesNotExist:
			usuario = None


		if usuario is not None:
			#Usuario.loginExtra(request, usuario)
			if id_user == '222':
				return redirect('JAlmacen')

			elif id_user == '987':
				return redirect('CRegistrado')

			elif id_user == '654':
				return redirect('Mozo')	

			elif id_user == '321':
				return redirect('Bartender')	

			elif id_user == '111':
				return redirect('Hostess')
			
			else:
				messages.info(request, 'Algùn dato es incorrecto. Vuelva a intentarlo.')
				return redirect('loginExtra')
		else:
			messages.info(request, 'Datos erroneos')
			return redirect('loginExtra')
	else:
		return render(request,'loginExtra.html')		
