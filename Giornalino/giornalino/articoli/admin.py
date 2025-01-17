from django.contrib import admin
from .forms import AccountSubscriberChangeForm
from .models import Articolo, NewsletterSubscriber, AccountSubscriber, MiPiace

#sistemazione aggiuntiva del database
class ArticoloAdmin(admin.ModelAdmin):
    #lista di attributi dell'articolo
    list_display = ('titolo', 'totale_mi_piace', 'autore', 'data_pubblicazione', 'id')

    #campi di ricerca
    search_fields = ('titolo', 'autore')

    list_filter = ('data_pubblicazione', 'autore')

    #ordinazione predefinita per data di pubblicazione
    ordering = ('data_pubblicazione',)

class AccountSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'data_iscrizione')
    form = AccountSubscriberChangeForm  # Usa il form personalizzato
    readonly_fields = ('data_iscrizione',)

    ordering = ('data_iscrizione',)

  
    
admin.site.register(Articolo, ArticoloAdmin)
admin.site.register(NewsletterSubscriber)
admin.site.register(AccountSubscriber, AccountSubscriberAdmin)
