from django.db import models
from AUTH.ModuleTaskManagement.models import Task, Module


class Role(models.Model):
    name = models.CharField(max_length=100, default='', blank=True)
    is_archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'AUTH_RoleCreation_Role'



class RoleModule(models.Model):
    role = models.ForeignKey(Role,on_delete=models.SET_NULL, null=True, blank=True)
    module = models.ForeignKey(Module,on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.role.name + '->' + self.module.name

    class Meta:
        db_table = 'AUTH_RoleCreation_RoleModule'



class RoleDistribution(models.Model):
    role = models.ForeignKey(Role,on_delete=models.SET_NULL, null=True, blank=True)
    task = models.ForeignKey(Task,on_delete=models.SET_NULL, null=True, blank=True)
    view_task = models.BooleanField(default=False)
    add_task = models.BooleanField(default=False)
    edit_task = models.BooleanField(default=False)
    delete_task = models.BooleanField(default=False)
    print_task = models.BooleanField(default=False)
    cancel_task = models.BooleanField(default=False)
    reset_task = models.BooleanField(default=False)
    find_task = models.BooleanField(default=False)
    save_task = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        if self.role and self.task:
            return self.role.name + ' ==> ' + self.task.name
        else:
            return 'Task / Role not available'

    class Meta:
        db_table = 'AUTH_RoleCreation_RoleDistribution'
