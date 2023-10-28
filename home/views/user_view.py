import json
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from home.forms.user_form import CustomAuthenticationForm, RegisterForm, RegisterUpdateForm, PasswordUpdateForm

from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model

# Create your views here.
@login_required(login_url='home:login')
def profile(request, pk):
    UserTable = get_user_model()
    user = UserTable.objects.get(pk=pk)

    return render(
        request,
        'user/profile.html',
        {
            'usuario': user            
        }
    )

@login_required(login_url='home:login')
def update(request, pk):

    UserTable = get_user_model()
    user = UserTable.objects.get(pk=pk)

    form = RegisterUpdateForm(instance=user)

    return render(
        request,
        'user/edit.html',
        {
            'form': form
        }
    )

def login(request):
    form = CustomAuthenticationForm(request)

    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Logado com sucesso!')
            return redirect('home:index')
        messages.error(request, 'Login inválido')

    return render(
        request,
        'default_pages/index.html',
        {
            'form': form
        }
    )

def logout(request):
    auth.logout(request)
    return redirect('home:login')

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário Registrado')
            return redirect('home:index')

    return render(
        request,
        'user/register.html',
        {
            'form': form
        }
    )

def change_password(request, pk):
    UserTable = get_user_model()
    user = UserTable.objects.get(pk=pk)
    form = PasswordUpdateForm(instance=user)

    if request.method == 'POST':
            form = PasswordUpdateForm(request.POST)

            if form.is_valid():
                user.set_password(request.POST.get('password1'))
                user.save()
                messages.success(request, 'Senha Alterada')
                return redirect('home:login')

    return render(
        request,
        'user/change_password.html',
        {
            'form': form
        }
    )