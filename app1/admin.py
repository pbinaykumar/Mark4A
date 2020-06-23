from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Contact


# Register your models here.
admin.site.register(Contact)

class cua(UserAdmin):
    list_display = ('username','email','first_name','last_name','is_staff','last_login')

admin.site.unregister(User)
admin.site.register(User,cua)