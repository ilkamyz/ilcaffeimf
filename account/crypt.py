from django.contrib.auth.hashers import make_password
from .models import AccountSubscriber

# Cripta tutte le password esistenti
for account in AccountSubscriber.objects.all():
    if account.password and not account.password.startswith('pbkdf2_'):  # Verifica se la password è già criptata
        account.password = make_password(account.password)
        account.save()
