from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    otp = models.IntegerField(default=None, null=True)
    username = models.CharField(max_length=40, default=None, null=True)
    mobile = models.BigIntegerField(default=None, null=True)
    gender = models.CharField(max_length=40, default=None, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
