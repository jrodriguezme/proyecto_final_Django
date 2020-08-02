from django.urls import path
from . import views
from usuario.views import loginExtra, CRegistrado, Bartender, Hostess, Mozo, JAlmacen
#app_name = 'usuario' 

urlpatterns=[
	path('loginExtra', loginExtra, name="loginExtra"),
	path('CRegistrado', views.CRegistrado, name="CRegistrado"),
	path('Bartender', Bartender, name="Bartender"),
	path('Hostess', Hostess, name="Hostess"),
	path('JAlmacen', views.JAlmacen, name="JAlmacen"),
	path('Mozo', Mozo, name="Mozo"),
	#path('', views.index, name="index"),
]