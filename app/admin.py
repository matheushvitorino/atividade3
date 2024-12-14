from django.contrib import admin
from .models import Usuario,Telefone

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_field = ('nome',)
    
@admin.register(Telefone)
class TelefoneAdmin(admin.ModelAdmin):
    list_display = ('id','usuario_id', 'numero')
    search_field = ('numero',)
