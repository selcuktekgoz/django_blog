from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import CustomUserModel


#! hepsini aldım + kendiminkini ilave ediyorum


@admin.register(CustomUserModel)
class CustomAdmin(UserAdmin):
    list_display = ("username", "email")
    fieldsets = UserAdmin.fieldsets + (("Avatarınız", {"fields": ["avatar"]}),)


# admin.site.register(CustomUserModel, CustomAdmin)
