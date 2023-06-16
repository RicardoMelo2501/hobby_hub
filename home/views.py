from django.shortcuts import render
from menu.models import Menu, SubMenu

# Create your views here.
def home(request):
    dataMenus = Menu.objects.all()
    dataSubMenus = SubMenu.objects.all()

    context = { 
        'menus': dataMenus, 
        'sub_menus': dataSubMenus 
    }

    return render(request, 'home/index.html', context)