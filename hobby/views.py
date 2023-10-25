from django.shortcuts import render
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from hobby.models import Hobby

# Create your views here.
# @login_required(login_url='home:login')
def index(request):
    hobbyObjects = Hobby.objects.all()
    # dataSubMenus = SubMenu.objects.all()

    context = { 
        'hobbies': hobbyObjects, 
        # 'sub_menus': dataSubMenus,
        # 'form' : myForm
    }

    return render(request, 'hobby/index.html', context)