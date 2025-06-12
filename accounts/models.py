import uuid
from datetime import timezone
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255 , unique=True)
    username = models.CharField(max_length=55)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True , null=True)
    updated = models.DateTimeField(auto_now=True , null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin

class EmailConfirmation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    key = models.UUIDField(default=uuid.uuid4, unique=True , editable=False)
    created = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)

    def is_valid(self):
        return not self.confirmed and (timezone.now() - self.created).total_seconds() < 5*60

    def confirm(self):
        if self.is_valid():
            self.confirmed = True
            self.user.is_active = True
            self.user.save()
            self.save()
            return True
        return False