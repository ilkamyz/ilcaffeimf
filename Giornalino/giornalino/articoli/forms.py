from django import forms
from .models import NewsletterSubscriber

#file creato apposta per il form di iscrizione
class NewsletterSubscriptionForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ['email']
