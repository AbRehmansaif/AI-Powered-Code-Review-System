from django.db import models
from django.utils.translation import gettext_lazy as _

class User(models.Model):
    user_name = models.CharField(
        unique=True, null=True,
        blank=True, verbose_name=_("User Name")
    )
    
    email = models.EmailField(
        null=True, blank=True,
        verbose_name=_("E-mail")
    )
    
    password_1 = models.CharField(
        null=True, blank=True,
        verbose_name=_("Password")
    )
    
    password_2 = models.CharField(
        null=True, blank=True,
        verbose_name=_("Confirm Password")
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    
    updated_at = models.DateTimeField(
        auto_now=True
    )
    
