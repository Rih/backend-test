# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from typing import Set
from django.contrib import admin
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission
from account.models import Role
# Register your models here.

admin.site.register(Permission)

# Unregister the provided model admin
# admin.site.unregister(User)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    readonly_fields = ('date_joined',)
    exclude = ('date_joined',)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        disabled_fields = set()  # type: Set[str]

        if not is_superuser:
            disabled_fields |= {
                'username',
                'is_superuser',
                'user_permissions',
            }

        # Prevent non-superusers from editing their own permissions
        if (
            not is_superuser
            and obj is not None
            and obj == request.user
        ):
            disabled_fields |= {
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            }

        for f in disabled_fields:
            if f in form.base_fields:
                form.base_fields[f].disabled = True

        return form


from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group



admin.site.unregister(Group)
admin.site.register(Role, GroupAdmin)