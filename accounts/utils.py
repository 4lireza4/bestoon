from .models import User , EmailConfirmation
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse


def send_confirmation_email(user , request):
    confirmation = EmailConfirmation.objects.create(user=user)
    relative_url = reverse('client_accounts:confirm_email', kwargs={'key': confirmation.key})
    confirm_url = request.build_absolute_uri(relative_url)

    send_mail(
        'Confirm Your Email',
        f'Click this link to confirm your email: {confirm_url}',
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False,
    )