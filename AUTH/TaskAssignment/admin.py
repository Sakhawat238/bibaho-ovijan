from django.contrib import admin
from .models import UserWithRole,UserWithTask,UserWithModule

admin.register(UserWithTask,UserWithRole,UserWithModule)(admin.ModelAdmin)
