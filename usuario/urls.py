from django.urls import path
from . import views
from usuario.views import loginExtra

urlpatterns=[
	path('loginExtra', loginExtra, name="loginExtra"),
	#path('', views.index, name="index"),
]