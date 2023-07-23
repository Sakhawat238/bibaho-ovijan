from django.db import models




class SuccessStories(models.Model):
    code = models.CharField(max_length=20,null=False,unique=True)
    created_by = models.CharField(max_length=50,default="")
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    is_archived = models.BooleanField(default=False)
    
    def __str__(self):
        return self.code

    class Meta:
        db_table = 'Matrimony_Profile'




