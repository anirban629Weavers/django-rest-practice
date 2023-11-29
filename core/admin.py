from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id","username","name","email","is_superuser")
    list_display_links= ("username","id","email")
    list_editable = ("is_superuser",)

# admin.site.register(CustomUser,UserAdmin) 
