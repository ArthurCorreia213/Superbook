from django.contrib import admin
from .models import Heroi

# Register your models here.

@admin.register(Heroi)
class HeroiAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'poderes', 'estado', 'cidade', 'date_joined']
    list_filter = ['cidade']
    search_fields = ['username', 'cidade', 'estado']

    fieldsets = (
        (
            'Identidade', {
                'fields': ('username',)
            }
        ),
        (
            'Informações Gerais', {
                'fields': ('email', 'poderes', 'cidade', 'estado')
            }
        ),
        (
            'Dados de registro', {
                'fields': ('date_joined', 'is_superuser')
            }
        )
    )
    readonly_fields = ['date_joined', 'is_superuser']