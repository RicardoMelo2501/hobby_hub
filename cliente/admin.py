from django.contrib import admin

from cliente.models import Cliente

# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = 'nome', 'cpf_cnpj',