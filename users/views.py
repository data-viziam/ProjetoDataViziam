from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'users/users.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso! Faça login.')
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('senha')
        
        # Verificar se o e-mail foi preenchido
        if not email:
            messages.error(request, 'O campo e-mail é obrigatório.', extra_tags='email')
            return render(request, 'users/login.html')
        
        # Verificar se a senha foi preenchida
        if not password:
            messages.error(request, 'O campo senha é obrigatório.', extra_tags='senha')
            return render(request, 'users/login.html')
        
        # Autenticar o usuário
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('profile')  # Redireciona para a página de perfil após o login
        else:
            messages.error(request, 'E-mail ou senha incorretos. Tente novamente.', extra_tags='senha')
    
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')  # Redireciona para a página inicial após o logout

@login_required
def profile_view(request):
    return render(request, 'users/profile.html', {'user': request.user})