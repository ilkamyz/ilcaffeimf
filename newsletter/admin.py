from django.contrib import admin
from .models import IscrizioneNewsletter

@admin.register(IscrizioneNewsletter)
class IscrizioneNewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'data_iscrizione', 'is_active')  # Campi da mostrare nel pannello admin
    list_filter = ('is_active', 'data_iscrizione')            # Filtro per visualizzare meglio i dati
    search_fields = ('email',)                               # Campo per cercare gli utenti iscritti

