from django.urls import path
from . import views
#from django.contrib.auth.views import login, password_reset, password_reset_done, password_confirm, password_reset_confirm, password_reset_complete

urlpatterns = [
    path('register', views.register, name="register"), 
   	path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("administrar", views.administrar, name="administrar"),
    path("book", views.book, name="book"),    
    path("platos", views.menu, name="platos"),
    path("id", views.id, name="id"),    
    path("loginExtra", views.loginExtra, name="loginExtra"),    
    path("gerente", views.gerente, name="gerente"),        
  #   path("reset/password_reset", views.password_reset, {'template_name':'usuario/password_reset_form.html', 
  #   	'email_template': 'registration/password_reset_email.html'}, name="password_reset"),        
  #   path("reset/password_reset_done", views.password_reset_done, {'template_name':'registration/password_reset_done.html'}, 
		# name="password_reset_done"),          
  #   path("reset/(?P<uidb64>[0-9A-Za-z\-+])/(?P<token>.+)/$", views.password_reset.confirm, 
  #   	{'template_name':'registration/password_reset_confirm.html' }, name="password_reset_confirm"),
  #   path("reset/done", views.password_reset_complete, 
  #   	{'template_name':'registration/password_reset_complete.html'}, name="password_reset_complete"),       	       
] 
