from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        (
            'Extra information',
            {
                'fields': ('image',)
            },
        ),
    )


admin.site.register(User, UserAdmin)
