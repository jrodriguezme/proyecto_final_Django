from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.
from persona.views import Personal
def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username, password=password )		

		if user is not None:
			auth.login(request, user)
			return redirect('gerente')
		else: 
			messages.info(request, 'Datos erroneos')
			return redirect('login')
	else:
		return render(request, 'login.html')		

def register(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		password1 = request.POST['password1']
		password2 = request.POST['password2']		
		email = request.POST['email']

		if password1 == password2:
			if User.objects.filter(username=username).exists():
				messages.info(request, 'El usuario ya esta siendo utilizado')
				return redirect('register')
			elif User.objects.filter(email=email).exists():
				messages.info(request, 'El correo ya esta siendo utilizado')
				return redirect('register')
			else:
				user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
				user.save();
				print('user created')
				return redirect('login')
		else:
			messages.info(request, 'las contraseñas no coinciden')
			return redirect('register')
		return redirect('/')
	else:
		return render(request, 'register.html')


def logout(request):
	auth.logout(request)
	return redirect('/')

def administrar(request):
	return render(request, 'base.html')

def book(request):
	return render(request, 'reservation.html') 

def menu(request): 
	return render(request, 'platos.html') 

def id(request): 
	if request.method == 'POST':
		id_user = request.POST['id_user']

		if id_user == '999':
			return redirect("login")
			return render(request, 'login.html')
			
		elif id_user == '990':
			return redirect("loginExtra")			
			return render(request, 'loginExtra.html')

		elif id_user == '988':
			return redirect("loginExtra")			
			return render(request, 'loginExtra.html')

		elif id_user == '987':
			return redirect("loginExtra")			
			return render(request, 'loginExtra.html')

		elif id_user == '654':
			return redirect("loginExtra")
			return render(request, 'loginExtra.html')

		elif id_user == '321':
			return redirect("loginExtra")
			return render(request, 'loginExtra.html')

		elif id_user == '111':
			return redirect("loginExtra")
			return render(request, 'loginExtra.html')

		elif id_user == '222':
			return redirect("loginExtra")
			return render(request, 'loginExtra.html')

		else:
			messages.info(request, 'El id no existe. Intente nuevamente.')
			return redirect('id')
	else:
		return render(request, 'id.html') 


# def loginExtra(request): 
# 	return render(request, 'loginExtra.html') 

def gerente(request):
 	return render(request, 'indexGerente.html')	

# def Bartender(request):
# 	return render(request, 'indexBartender.html')

#def CRegistrado(request):
# 	return render(request, 'indexCRegistrado.html')

# def Cajero(request):
# 	return render(request, 'indexCajero.html')

# def JAlmacen(request):
# 	return	render(request, 'indexJAlmacen.html')

# def Mozo(request):
# 	return render(request, 'indexMozo.html')	

# def JCocina(request):
# 	return render(request, 'indexJCocina.html')	
 
# def Administrador(request):
# 	return render(request, 'usuario/indexAdministrador.html')	

# def loginExtra(request):
# 	if request.method == 'POST':
# 		id_trabajo = request.POST['id_user']
# 		dni 	= request.POST['username']
# 		password= request.POST['password']

# 		#person = Personal.objects.get(username=dni, password=password, id_user=id_trabajo)		
# 		#person = Personal.authenticate(username=dni, password=password, id_user=id_user)		
# 		try:
# 		    person = Personal.objects.get(username=dni, password=password, id_trabajo=id_trabajo)
# 		except Personal.DoesNotExist:
# 		 	person = None


# 		if person is not None:
# 			if id_user == '987':
# 				return redirect('JAlmacen')

# 			elif id_user == '990':
# 				return redirect('Administrador')
			
# 			elif id_user == '988':
# 				return redirect('JCocina')

# 			elif id_user == '222':
# 				return redirect('CRegistrado')
			
# 			elif id_user == '654':
# 				return redirect('Mozo')	

# 			elif id_user == '321':
# 				return redirect('Bartender')	

# 			elif id_user == '111':
# 				return redirect('Cajero')
			
# 			else:
# 				messages.info(request, 'Algùn dato es incorrecto. Vuelva a intentarlo.')
# 				return redirect('loginExtra')
# 		else:
# 			messages.info(request, 'Datos erroneos')
# 			return redirect('loginExtra')
# 	else:
# 		return render(request,'loginExtra.html')		


# def registerExtra(request):
# 	return render(request, 'registerExtra.html')	