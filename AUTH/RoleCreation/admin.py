from django.contrib import admin
from django.db import models
from .models import Role,RoleDistribution, RoleModule

admin.register(Role,RoleDistribution, RoleModule)(admin.ModelAdmin)