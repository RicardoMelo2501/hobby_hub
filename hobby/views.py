from django.shortcuts import render
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from hobby.models import Hobby

# Create your views here.
@login_required(login_url='home:login')
def index(request):
    hobbyObjects = Hobby.objects.all()
    current_user = request.user

    context = { 
        'hobbies': hobbyObjects,
        'usuario_logado': current_user
    }

    return render(request, 'hobby/index.html', context)