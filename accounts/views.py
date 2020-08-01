from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username, password=password )		

		if user is not None:
			auth.login(request, user)
			return redirect("/")
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


def loginExtra(request): 
	return render(request, 'loginExtra.html') 