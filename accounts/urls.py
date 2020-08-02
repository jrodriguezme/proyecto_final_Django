from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name="register"), 
   	path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("administrar", views.administrar, name="administrar"),
    path("book", views.book, name="book"),    
    path("platos", views.menu, name="platos"),
    path("id", views.id, name="id"),    
    path("loginExtra", views.loginExtra, name="loginExtra"),    
] 
