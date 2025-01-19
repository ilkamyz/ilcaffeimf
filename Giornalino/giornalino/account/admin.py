from django.contrib import admin
from .models import AccountSubscriber
from .forms import AccountSubscriberChangeForm
# Register your models here.

class AccountSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'data_iscrizione')
    form = AccountSubscriberChangeForm  # Usa il form personalizzato
    readonly_fields = ('data_iscrizione',)

    ordering = ('data_iscrizione',)

admin.site.register(AccountSubscriber, AccountSubscriberAdmin)
