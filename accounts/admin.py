from django.contrib import admin
from .models import Accounts, UserProfile
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

# Create Your Model here
class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'date_joined', 'last_login',)
    list_display_links = ('email', 'first_name', 'last_name',)
    readonly_fields = ('date_joined', 'last_login',)
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class UserProfileAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.profile_picture.url))
    thumbnail.short_description = 'Profile Picture'
    list_display = ('thumbnail', 'user', 'city', 'state', 'country')



# Register your models here.
admin.site.register(Accounts, AccountAdmin)
admin.site.register(UserProfile, UserProfileAdmin)