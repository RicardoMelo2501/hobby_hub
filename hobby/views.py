from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from hobby.models import Hobby, Categoria, Participante
from django.contrib.auth.models import User
from django.core.paginator import Paginator

# Create your views here.
@login_required(login_url='home:login')
def index(request):
    current_user = request.user
    valor_filtro = ''
    CategoriaObjects = Categoria.objects.all()
    # TODOS OS HOBBIES
    hobbyObjects = Hobby.objects.all()
    # HOBBIES QUE EU CADASTREI
    hobbyParticipandoCriado = Hobby.objects.filter(usuario=current_user)
    # HOBBIES QUE EU ME INSCREVI
    participantes_do_usuario = Participante.objects.filter(user_participante=current_user)
    # Acesse os objetos Hobby relacionados aos Participantes do usuário
    hobbyParticipandoRegistrado_list = Hobby.objects.filter(participantes__in=participantes_do_usuario)

    if request.method == 'POST' and request.POST.get('filtro') != "" :
        valor_filtro = request.POST.get('filtro')
        # TODOS OS HOBBIES
        hobbyObjects = Hobby.objects.filter(nome__icontains=request.POST.get('filtro'))
        # HOBBIES QUE EU CADASTREI
        hobbyParticipandoCriado = Hobby.objects.filter(nome__icontains=request.POST.get('filtro'))
        # HOBBIES QUE EU ME INSCREVI
        participantes_do_usuario = Participante.objects.filter(user_participante=current_user)
        # Acesse os objetos Hobby relacionados aos Participantes do usuário
        hobbyParticipandoRegistrado_list = Hobby.objects.filter(participantes__in=participantes_do_usuario, nome__icontains=request.POST.get('filtro'))

    paginator  = Paginator(hobbyObjects, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = { 
        'valor_filtro': valor_filtro,
        'categorias': CategoriaObjects,
        'hobbies': hobbyObjects,
        'hobbies_participando_criado': hobbyParticipandoCriado,
        'hobbies_participando_registrado': hobbyParticipandoRegistrado_list,
        'usuario_logado': current_user,
        "page_obj": page_obj
    }

    return render(request, 'hobby/index.html', context)

# Create your views here.
@login_required(login_url='home:login')
def list_hobby(request):
    current_user = request.user
    valor_filtro = ''
    CategoriaObjects = Categoria.objects.all()
    # TODOS OS HOBBIES
    hobbyObjects = Hobby.objects.all()

    if request.method == 'POST' and request.POST.get('filtro') != "" :
        valor_filtro = request.POST.get('filtro')
        # TODOS OS HOBBIES
        hobbyObjects = Hobby.objects.filter(nome__icontains=request.POST.get('filtro'))

    paginator  = Paginator(hobbyObjects, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = { 
        'valor_filtro': valor_filtro,
        'categorias': CategoriaObjects,
        'hobbies': hobbyObjects,
        'usuario_logado': current_user,
        "page_obj": page_obj
    }

    return render(request, 'hobby/list.html', context)

def add_participacao(request, pk):
    current_user = request.user

    hobby_escolhido = Hobby.objects.get(id=pk)
    usuario = User.objects.get(id=current_user.id)

    new_participacao = Participante(hobby=hobby_escolhido, user_participante=usuario)
    new_participacao.save()
    return redirect('home:index')

def add(request) :

    current_user = request.user
    CategoriaObjects = Categoria.objects.all()

    if request.method == 'POST':

        if request.FILES.get('imagem'):
            imagem = request.FILES.get('imagem')
        else :
            imagem = 'sistema/default.webp'
        
        categoria = Categoria.objects.get(id=request.POST.get('categoria'))
        usuario = User.objects.get(id=current_user.id)
                                                            
        new_hobby = Hobby(
            nome=request.POST.get('nome'),
            local=request.POST.get('local'),
            data=request.POST.get('data'),
            time=request.POST.get('time'),
            imagem=imagem,
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

def delete(request, pk):

    hobbyObject = Hobby.objects.get(id=pk)
    hobbyObject.delete()

    return redirect('home:index')