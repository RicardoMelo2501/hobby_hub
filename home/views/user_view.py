from django.shortcuts import render, redirect
from menu.models import Menu, SubMenu

from django.contrib import auth, messages
from menu.forms import myForm
from home.forms.user_form import CustomAuthenticationForm, RegisterForm, RegisterUpdateForm

from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model

# Create your views here.
@login_required(login_url='home:login')
def index(request):
    User = get_user_model()
    users = User.objects.all()

    return render(
        request,
        'user/list.html',
        {
            'usuarios': users
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
        'user/login.html',
        {
            'form': form
        }
    )

def logout(request):
    auth.logout(request)
    return redirect('home:login')

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


# @login_required(login_url='home:login')
def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário registrado')
            return redirect('home:login')

    return render(
        request,
        'user/register.html',
        {
            'form': form
        }
    )