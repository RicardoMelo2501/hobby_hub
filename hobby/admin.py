from django.contrib import admin
from hobby.models import Hobby, Categoria

# Register your models here.
# Register your models here.
@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display = 'nome', 'local'
    # search_fields = 'id'
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = 'nome',
    # search_fields = 'id'