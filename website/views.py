from django.shortcuts import render

def home(request):
    return render(request, 'website/index.html')

def sobre(request):
    return render(request, 'website/about.html')

def contato(request):
    return render(request, 'website/contact.html')

def login(request):
    return render(request, 'website/login.html')

def login(request):
    return render(request, 'website/new_user_login.html')