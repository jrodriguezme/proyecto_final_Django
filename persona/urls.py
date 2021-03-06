"""primerProyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from accounts import views
from accounts.views import administrar
from .views import(
	PersonalListView, PersonalDetailView, PersonalCreateView,
	PersonalUpdateView, PersonalDeleteView,
	ClienteListView, ClienteDetailView, ClienteCreateView, 
	ClienteUpdateView, ClienteDeleteView,
	ProveedorListView, ProveedorDetailView, ProveedorCreateView, 
	ProveedorUpdateView, ProveedorDeleteView, loginExtra, 
    registerExtra, gracias, PDFPersonal, PDFCliente, PDFProveedor,
    Bartender, CRegistrado, Cajero, JAlmacen, JCocina, Mozo, Administrador
	) 

app_name = 'persona' 
 
urlpatterns = [
    path('', views.administrar, name='administrar'),

    path('personal/', PersonalListView.as_view(), name='personal-list'),
    path('personal/<int:pk>/', PersonalDetailView.as_view(), name='personal-detail'),
    path('personal/create/', PersonalCreateView.as_view(), name='personal-create'),
    path('personal/<int:pk>/update/', PersonalUpdateView.as_view(template_name='persona/personal_update.html'), name='personal-update'),
    path('personal/<int:pk>/delete/', PersonalDeleteView.as_view(), name='personal-delete'),
    path('personal/Bartender/', Bartender, name="Bartender"),
    path('personal/Cajero/', Cajero, name="Cajero"),
    path('personal/JCocina/', JCocina, name="JCocina"),
    path('personal/Administrador/', Administrador, name="Administrador"),
    path('personal/JAlmacen/', JAlmacen, name="JAlmacen"),
    path('personal/Mozo/', Mozo, name="Mozo"),
    path('personal/pdf/', PDFPersonal.as_view()),

    path('cliente/', ClienteListView.as_view(), name='cliente-list'),
    path('cliente/<int:pk>/', ClienteDetailView.as_view(), name='cliente-detail'),
    path('cliente/create/', ClienteCreateView.as_view(), name='cliente-create'),
    path('cliente/<int:pk>/update/', ClienteUpdateView.as_view(template_name='persona/cliente_update.html'), name='cliente-update'),
    path('cliente/<int:pk>/delete/', ClienteDeleteView.as_view(), name='cliente-delete'),
    path('cliente/pdf/', PDFCliente.as_view()),
    path('cliente/CRegistrado/', CRegistrado, name="CRegistrado"),

    path('proveedor/', ProveedorListView.as_view(), name='proveedor-list'),
    path('proveedor/<int:pk>/', ProveedorDetailView.as_view(), name='proveedor-detail'),
    path('proveedor/create/', ProveedorCreateView.as_view(), name='proveedor-create'),
    path('proveedor/<int:pk>/update/', ProveedorUpdateView.as_view(template_name='persona/proveedor_update.html'), name='proveedor-update'),
    path('proveedor/<int:pk>/delete/', ProveedorDeleteView.as_view(), name='proveedor-delete'),
    path('proveedor/pdf/', PDFProveedor.as_view()),

    path('personal/loginExtra/', loginExtra, name="loginExtra"),
    #path('cliente/registerExtra/', registerExtra, name="registerExtra"), 
    path('personal/gracias/', gracias, name="gracias"), 

]
