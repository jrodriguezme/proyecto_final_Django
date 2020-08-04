from django.urls import path
from . import views
from usuario.views import loginExtra, registerExtra, CRegistrado, Bartender, Cajero, Mozo, JAlmacen, JCocina, Administrador 

urlpatterns=[
	path('loginExtra', loginExtra, name="loginExtra"),
	path('registerExtra', registerExtra, name="registerExtra"),	
	path('CRegistrado', views.CRegistrado, name="CRegistrado"),
	path('Bartender', views.Bartender, name="Bartender"),
	path('Cajero', views.Cajero, name="Cajero"),
	path('JAlmacen', views.JAlmacen, name="JAlmacen"),
	path('JCocina', views.Mozo, name="JCocina"),
	path('Administrador', views.Administrador, name="Administrador"),
	path('Mozo', views.Mozo, name="Mozo"),
]