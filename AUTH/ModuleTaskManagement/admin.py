from django.contrib import admin
from .models import Module, SubModule,Task

admin.register(Module,SubModule,Task)(admin.ModelAdmin)
