from django.shortcuts import render

import random

def index_page(request):

    
    return render(request, 'index.html', {'eredmeny': (21312*123) })

def login_page(request):
    return render(request, 'login.html')