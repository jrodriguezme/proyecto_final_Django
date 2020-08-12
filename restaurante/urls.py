"""restaurante URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import GeneratePDF 
# from django.contrib.auth import password_reset
 
urlpatterns = [
	path('', include('feliciano.urls')),
    path('admin/', admin.site.urls),
    path('persona/', include('persona.urls')),
    path('accounts/', include('accounts.urls')),
    path('platos/', include('platos.urls')),
    path('comandas/',include('comandas.urls')),
    path('reporte/',include('reporte.urls')),
    path('pdf/', GeneratePDF.as_view()),

#     path("reset/password_reset", password_reset, {'template_name':'registration/password_reset_form.html', 
#         'email_template': 'usuario/password_reset_email.html'}, name='password_reset'),        
#     path("reset/password_reset_done", views.password_reset_done, {'template_name':'usuario/password_reset_done.html'}, 
#         name="password_reset_done"),          
#     path("reset/(?P<uidb64>[0-9A-Za-z\-+])/(?P<token>.+)/$", views.password_reset.confirm, 
#         {'template_name':'usuario/password_reset_confirm.html' }, name="password_reset_confirm"),
#     path("reset/done", auth_views.password_reset_complete, 
#         {'template_name':'usuario/password_reset_complete.html'}, name="password_reset_complete"),  
 ]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
