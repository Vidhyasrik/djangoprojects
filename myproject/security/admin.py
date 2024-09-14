from django.contrib import admin
from .models import MyUser

# Register your models here.

# class MyUserAdmin(admin.ModelAdmin):
#     fields = ['username', 'first_name', 'last_name', 'email']
admin.site.register(MyUser)