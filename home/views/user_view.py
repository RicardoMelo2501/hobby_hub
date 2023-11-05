import json
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from home.forms.user_form import CustomAuthenticationForm, RegisterForm, RegisterUpdateForm, PasswordUpdateForm, PasswordForgotForm

from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model

# Foto do user
from home.models import UserProfile

# Create your views here.
@login_required(login_url='home:login')
def profile(request, pk):
    UserTable = get_user_model()
    user = UserTable.objects.get(pk=pk)
    try:
        photo = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        photo = None

    if request.method == 'POST':
        if UserProfile.objects.get(user=user) :
            UserProfile.objects.get(user=user).delete()

        avataObject = UserProfile(user=user, avatar=request.FILES.get('avatar'))
        avataObject.save()

        return redirect('home:index')
    
    return render(
        request,
        'user/profile.html',
        {
            'usuario': user,
            'photo': photo            
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

@login_required(login_url='home:login')
def delete(request, pk):
    UserTable = get_user_model()
    user = UserTable.objects.get(pk=pk)
    user.delete()
    return redirect('home:login')

@login_required(login_url='home:login')
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

def forgot_password(request):
    UserTable = get_user_model()
    form = PasswordForgotForm()

    if request.method == 'POST':
            form = PasswordForgotForm(request.POST)
            user = UserTable.objects.get(email=request.POST.get('email'))

            if form.is_valid():
                user.set_password(request.POST.get('password1'))
                user.save()
                messages.success(request, 'Senha Alterada')
                return redirect('home:login')

    return render(
        request,
        'user/forgot_password.html',
        {
            'form': form
        }
    )