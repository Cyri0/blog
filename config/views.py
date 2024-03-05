from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from blogpost.models import BlogPost

@login_required(login_url='login/')
def index_page(request):
    posts = BlogPost.objects.all()
    return render(request, 'index.html', {'posts': posts })

def logout_page(request):
    logout(request)
    return redirect('index')

def login_page(request):
    if request.method == 'POST': # VANNAK BELÉPÉSI ADATOK
        form = AuthenticationForm(data = request.POST)

        if form.is_valid():
            uname = form.cleaned_data.get('username')
            pword = form.cleaned_data.get('password')
            user = authenticate(request, username=uname, password=pword)
            if user is not None:
                login(request, user)
                return redirect('index')
        return render(request, 'login.html')
    
    else: # ELŐSZÖR JÁR A LOGIN OLDALON
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})