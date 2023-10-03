from django.urls import path
from . import views

#urlconf 
urlpatterns = [
    path('', views.index),
    path('counter', views.counter, name='counter'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('Logout', views.Logout, name='Logout'),
    path('post/<str:pk>', views.post, name='post'),
    
]