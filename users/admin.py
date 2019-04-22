from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .models import CustomUser


class UserAdmin(BaseUserAdmin):
	add_fieldsets = (
		(None, {
			'fields': ('username', 'email', 'first_name', 'last_name', 'wishlists')
		}),
		('Permissions', {
			'fields': ('is_superuser', 'is_staff')
		})
	)
	fieldsets = (
		(None, {
			'fields': ('username', 'email', 'first_name', 'last_name', 'wishlists')
		}),
		('Permissions', {
			'fields': ('is_superuser', 'is_staff')
		})
	)
	list_display = ['username', 'email', 'first_name', 'last_name']
	search_fields = ('username', 'email', 'first_name', 'last_name')
	ordering = ('username',)


admin.site.register(CustomUser, UserAdmin)
admin.site.unregister(Group)
