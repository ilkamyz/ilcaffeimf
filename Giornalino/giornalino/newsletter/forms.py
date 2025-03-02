from django import forms
from .models import IscrizioneNewsletter

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = IscrizioneNewsletter
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Inserisci la tua email'}),
        }
