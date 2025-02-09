from django.contrib import admin
from .models import Articolo, MiPiace
from ckeditor.widgets import CKEditorWidget
from django import forms


class ArticoloForm(forms.ModelForm):
    class Meta:
        model = Articolo
        fields = [
            "titolo",
            "autore",
            "id",
            "contenuto",
            "descrizione_breve",
            "immagine",
        ]
        widgets = {
            "contenuto": CKEditorWidget(),  # Assicurati che 'contenuto' sia il campo che utilizza CKEditor
        }


class ArticoloAdmin(admin.ModelAdmin):
    form = ArticoloForm
    search_fields = ("titolo", "autore")
    list_filter = ("data_pubblicazione", "autore")
    ordering = ("-data_pubblicazione",)
    # lista di attributi dell'articolo
    list_display = ("titolo", "totale_mi_piace", "autore", "data_pubblicazione", "id")
    readonly_fields = ("data_pubblicazione",)

    class Media:
        js = ("https://cdn.ckeditor.com/ckeditor4/ckeditor.js",)

    # campi di ricerca


admin.site.register(Articolo, ArticoloAdmin)
