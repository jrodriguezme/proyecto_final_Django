from django.urls import path
from . import views

app_name = 'comandas' 

urlpatterns = [
	path('',views.comanda, name='comanda')
]
