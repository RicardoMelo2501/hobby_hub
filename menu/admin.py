from django.contrib import admin
from menu.models import Menu
from menu.models import SubMenu
from django.contrib import admin

from home.models import UserProfile
# Register your models here.

admin.site.register(UserProfile)

# Register your models here.
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = 'id', 'text', 'url_or_path', 'font_awesome_icon', 'new_tab'
    search_fields = 'id',
    # list_per_page = 1
    # Edição Rápida
    # list_editable = 'text',
    # list_display_links = 'text',
    
@admin.register(SubMenu)
class MenuAdmin(admin.ModelAdmin):
    list_display = 'id', 'text', 'url_or_path', 'font_awesome_icon', 'new_tab', 'parent_menu_id'