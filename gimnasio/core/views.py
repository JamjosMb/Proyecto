from django.http import HttpResponse
from django.shortcuts import render

# Create your views here


def home(request, template="home.html"):
    return render(request, template)

def products(request, template="products.html"):
    return render(request, template)


def servicios(request, template="servicios.html"):
    return render(request, template)
    
def login(request, template="login.html"):
    return render(request, template)

def contact(request, template="contact.html"):
    return render(request, template) 




