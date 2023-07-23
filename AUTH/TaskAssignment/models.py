from django.db import models
from AUTH.ModuleTaskManagement.models import Task, Module
from AUTH.RoleCreation.models import Role
from AUTH.UserAuthentication.models import User

import random
import string


def randomStringGenerator():
    name = "I"
    name = name + str(random.randint(100, 999))
    letters = string.ascii_uppercase
    name = name + ''.join(random.choice(letters) for i in range(2))
    name = name + str(random.randint(10, 99))
    name = name + ''.join(random.choice(letters) for i in range(2))
    name = name + str(random.randint(100, 999))
    name = name + "."
    return name


def upload_location(instance, filename):
    extension = filename.split(".")[1]
    changed_file_name = randomStringGenerator()
    return "%s/%s%s" % ("userimg", changed_file_name, extension)


class UserWithRole(models.Model):
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True,blank=True)
    role = models.ForeignKey(Role,on_delete=models.SET_NULL,null=True,blank=True)
    picture = models.ImageField(upload_to=upload_location, default='userimg/default.png')
    mobile = models.CharField(max_length=15,null=True,blank=True)
    is_archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        if self.user:
            return self.user.username
        else:
            return 'No user found'

    class Meta:
        db_table = 'AUTH_TaskAssignment_UserWithRole'



class UserWithModule(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    module = models.ForeignKey(Module,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        if self.user and self.module:
            return self.user.username + '-->' + self.module.name
        else:
            return 'No user found'

    class Meta:
        db_table = 'AUTH_TaskAssignment_UserWithModule'



class UserWithTask(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    task = models.ForeignKey(Task,on_delete=models.SET_NULL,null=True,blank=True)
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
        if self.user and self.task:
            return self.user.username+'->'+self.task.name
        else:
            return 'User / Task not available'

    class Meta:
        db_table = 'AUTH_TaskAssignment_UserWithTask'
