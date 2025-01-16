from django.core.mail import send_mail
from .models import NewsletterSubscriber

def send_newsletter(subject, message):
    subscribers = NewsletterSubscriber.objects.filter(is_active=True)
    emails = [subscriber.email for subscriber in subscribers]

    send_mail(
        subject,
        message,
        "mail.giornalino@lorenzo.com",  #sostituire con l'email del giornalino pls
        emails,
        fail_silently=False,
    )
