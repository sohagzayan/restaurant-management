from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import User, Post

# Custom UserAdmin for the custom User model
class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'name', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser')  # Add 'is_superuser' if you need it
    search_fields = ('email', 'name')
    readonly_fields = ('last_login',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),  # Add 'is_superuser'
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'is_staff', 'is_superuser', 'is_active'),
        }),
    )
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions')  # Only if you want to keep groups functionality

# Unregister the default Group model as it's not used in this setup
admin.site.unregister(Group)

# Register the custom User model with the custom UserAdmin
admin.site.register(User, UserAdmin)

# Register the Post model
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    search_fields = ('title', 'content')
