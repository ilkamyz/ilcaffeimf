from django.contrib import admin
from .models import Articolo, NewsletterSubscriber

#sistemazione aggiuntiva del database
class ArticoloAdmin(admin.ModelAdmin):
    #lista di attributi dell'articolo
    list_display = ('titolo', 'autore', 'data_pubblicazione', 'id')

    #campi di ricerca
    search_fields = ('titolo', 'autore')

    list_filter = ('data_pubblicazione', 'autore')

    #ordinazione predefinita per data di pubblicazione
    ordering = ('data_pubblicazione',)
    
admin.site.register(Articolo, ArticoloAdmin)
admin.site.register(NewsletterSubscriber)
