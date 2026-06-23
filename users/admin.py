from django.contrib import admin

# Register your models here.

from .models import User

# Register your models here.

@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active',)