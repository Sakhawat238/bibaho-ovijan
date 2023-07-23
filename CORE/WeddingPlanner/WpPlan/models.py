from django.db import models
from AUTH.UserAuthentication.models import User
from CORE.WeddingPlanner.WpService.models import Service


class Checklist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(default="")
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.first_name
    
    class Meta:
        db_table = 'core_wpplan_checklist'


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, default="")
    description = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.first_name
    
    class Meta:
        db_table = 'core_wpplan_note'


class Directory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    seller_info = models.CharField(max_length=500, default="")
    remarks = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.first_name
    
    class Meta:
        db_table = 'core_wpplan_directory'