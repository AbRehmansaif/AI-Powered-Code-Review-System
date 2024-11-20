from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    
    list_display = (
        'user_name', 'email', 
        'first_name', 'last_name', 
        'password_1', 'password_2',
        'is_active', 'created_at',
        'updated_at'
    )
    
    search_fields = ('user_name', 'email')

    fieldsets = (
        (None, {'fields': ('user_name', 'email', 'password')}),
        (_('Personal Info'), {
            'fields': ('first_name', 'last_name')
        }),
        (_('Permissions'), {
            'fields': (
                'is_active'
            )
        }),
        (_('Important dates'), {
            'fields': ('created_at', 'updated_at')
        }),
    )
    

admin.site.register(User, CustomUserAdmin)