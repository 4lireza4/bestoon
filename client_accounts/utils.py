from accounts.models import User , EmailConfirmation
from django.core.mail import send_mail
from django.conf import settings

def send_confirmation_email(user):
    confirmation = EmailConfirmation.objects.create(user=user)
    confirm_url = f"http://localhost:8000/clients/register/confirm-email/{confirmation.key}/"
    send_mail(
        'Confirm Your Email',
        f'Hi {user.username} Click this link to confirm your email: {confirm_url}',
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False,
    )