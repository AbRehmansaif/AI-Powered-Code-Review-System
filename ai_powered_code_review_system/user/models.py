from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        
    user_name = models.CharField(
        unique=True, max_length=150,
        blank=True, verbose_name=_("Username")
    )
    
    email = models.EmailField(
        unique=True,
        verbose_name=_("E-mail")
    )
    
    first_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name=_("First Name")
    )
    
    last_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name=_("Last Name")
    )
    
    password_1 = models.CharField(
        null=True, blank=True,
        verbose_name=_("Password")
    )
    
    password_2 = models.CharField(
        null=True, blank=True,
        verbose_name=_("Confirm Password")
    )
       
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Active Status")
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    
    updated_at = models.DateTimeField(
        auto_now=True
    )
    
    def __str__(self):
        return self.username
