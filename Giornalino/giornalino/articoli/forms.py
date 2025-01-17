from django import forms
from django.contrib.auth.hashers import make_password
from .models import NewsletterSubscriber, AccountSubscriber

#file creato apposta per il form di iscrizione alla newsletter
class NewsletterSubscriptionForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ['email']

#file per il form degli account
class AccountSubscriberChangeForm(forms.ModelForm):
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput,
        help_text="Lascia vuoto per mantenere la password attuale."
    )

    class Meta:
        model = AccountSubscriber
        fields = ('email', 'is_active', 'password')  # Mostra solo i campi rilevanti

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if password:
            return make_password(password)  # Cripta la password
        return self.instance.password  # Mantieni la password attuale
    