from django.shortcuts import render,redirect,get_object_or_404
from shop.models import *
from cart.models import *
from django.core.exceptions import ObjectDoesNotExist

def ac_login(request):
    return render(request,'login.html')

def ac_register(request):
    return render(request,'register.html')