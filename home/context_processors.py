from menu.models import Menu, SubMenu

def default_context_values(request):
    dataMenus = Menu.objects.all()
    dataSubMenus = SubMenu.objects.all()
    
    return { 
        'menus': dataMenus, 
        'sub_menus': dataSubMenus,
    }