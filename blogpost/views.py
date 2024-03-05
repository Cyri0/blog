from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from .models import BlogPost

# Create your views here.
def changeBlogpost(request):
    if request.method != 'POST':
        return JsonResponse({'message':'Only POST allowed!'})
    
    id = request.POST['id']
    new_content = request.POST['new_content']
    bpost = BlogPost.objects.get(id = id)

    bpost.content = new_content
    bpost.save()
    return redirect('index')
