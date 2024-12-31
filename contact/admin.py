from django.contrib import admin
from contact import models

# Register your models here.


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    # Itens que serão exibidos na tela de administração
    list_display = (
        'id',
        'first_name',
        'last_name',
        'phone',
    )

    # Ordem dos itens na tela de administração
    ordering = ('-id',)

    # Filtro dos itens na tela de administração
    # list_filter = ('created_date',)

    # Busca dos itens na tela de administração
    search_fields = (
        'id',
        'first_name',
        'last_name'
    )

    # Quantidade de itens por página na tela de administração
    list_per_page = 20

    # Quantidade máxima de itens na tela de administração
    list_max_show_all = 200

    # Editar os itens na tela de administração
    list_editable = (
        'first_name',
        'last_name',
    )

    # Link de edição nos itens na tela de administração
    list_display_links = (
        'id',
        'phone',
    )
