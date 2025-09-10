
from django.contrib import admin
from .models import Villain

@admin.register(Villain)
class VillainAdmin(admin.ModelAdmin):
    list_display = ['codinome', 'nome_real', 'poderes', 'cidade', 'criado_em']
    list_filter = ['cidade']
    search_fields = ['codinome', 'nome_real', 'cidade']

    fieldsets = (
        ('Identidade Secreta', {
            'fields': ('codinome', 'nome_real')
        }),
        ('Informações Gerais', {
            'fields': ('poderes', 'cidade', 'historia')
        }),
        ('Dados de Registro', {
            'fields': ('criado_em',)
        }),
    )
    readonly_fields = ['criado_em']

