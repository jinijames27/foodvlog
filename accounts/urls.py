from django.urls import path
from . import views

urlpatterns=[
    path('login',views.ac_login,name='login'),
    path('register',views.ac_register,name='register'),

]