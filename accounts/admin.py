from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Create Your Model here
class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'date_joined', 'last_login',)
    list_display_links = ('email', 'first_name', 'last_name',)
    readonly_fields = ('date_joined', 'last_login',)
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()



# Register your models here.
admin.site.register(Accounts, AccountAdmin)