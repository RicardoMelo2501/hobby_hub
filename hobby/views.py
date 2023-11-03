from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from hobby.models import Hobby, Categoria
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='home:login')
def index(request):
    current_user = request.user
    
    hobbyObjects = Hobby.objects.all()
    hobbyParticipando = Hobby.objects.filter(usuario=current_user)

    context = { 
        'hobbies': hobbyObjects,
        'hobbies_participando': hobbyParticipando,
        'usuario_logado': current_user
    }

    return render(request, 'hobby/index.html', context)

def add(request) :

    current_user = request.user
    CategoriaObjects = Categoria.objects.all()

    if request.method == 'POST':
        
        categoria = Categoria.objects.get(id=request.POST.get('categoria'))
        usuario = User.objects.get(id=current_user.id)
                                                            
        new_hobby = Hobby(
            nome=request.POST.get('nome'),
            local=request.POST.get('local'),
            data=request.POST.get('data'),
            time=request.POST.get('time'),
            imagem=request.FILES.get('imagem'),
            categoria = categoria,
            descricao=request.POST.get('descricao'),
            usuario=usuario,
        )

        new_hobby.save()

        return redirect('home:index')

    context = {  
        'usuario_logado': current_user,
        'categorias': CategoriaObjects
    }

    return render(request, 'hobby/cadastrar.html', context)