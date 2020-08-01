from django.urls import path
from . import views

urlpatterns=[
	path('',views.index, name="index"),
	path('nosotros',views.nosotros, name="nosotros"),
	path('blog',views.blog, name="blog"),
	path('contactanos',views.contactanos, name="contactanos"),
	path('menu',views.menu, name="menu"),
]