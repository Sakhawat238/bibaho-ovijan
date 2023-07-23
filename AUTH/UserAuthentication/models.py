import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class USER_TYPE(models.TextChoices):
    ADMIN = 'admin'
    VISITOR = 'visitor'
    SELLER = 'seller'


class User(AbstractUser):
    slug = models.CharField(max_length=255, default=uuid.uuid4, null=True, blank=True)
    type = models.CharField(max_length=255, choices=USER_TYPE.choices)
    mobile = models.CharField(max_length=32, blank=True, null=True)
    mobile_verified = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username + ' -> ' + self.type


    # @property
    # def user_object(self):
    #     if self.type == USER_TYPE.EMPLOYEE:
    #         return self.employee
    #     if self.type == USER_TYPE.EMPLOYER:
    #         return self.employer

    # @property
    # def is_employee(self):
    #     if self.type == USER_TYPE.EMPLOYEE:
    #         return True
    #     return False

    # @property
    # def is_employer(self):
    #     if self.type == USER_TYPE.EMPLOYER:
    #         return True
    #     return False

    # @property
    # def is_admin(self):
    #     if self.type != USER_TYPE.EMPLOYEE and self.type != USER_TYPE.EMPLOYER:
    #         return True
    #     return False

    # @property
    # def getShortName(self):
    #     if self.type == USER_TYPE.EMPLOYEE:
    #         n = self.employee.name.split(' ')
    #         return ''.join(x[0]+'. ' for x in n[:-1])+n[-1]
    #     if self.type == USER_TYPE.EMPLOYER:
    #         return self.employer.name.split(' ')[0]

