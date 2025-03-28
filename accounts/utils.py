from .models import User , EmailConfirmation
from django.core.mail import send_mail
from django.conf import settings

def send_confirmation_email(user):
    confirmation = EmailConfirmation.objects.create(user=user)
    confirm_url = f"http://localhost:8000/accounts/confirm-email/{confirmation.key}/"
    send_mail(
        'Confirm Your Email',
        f'Click this link to confirm your email: {confirm_url}',
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False,
    )