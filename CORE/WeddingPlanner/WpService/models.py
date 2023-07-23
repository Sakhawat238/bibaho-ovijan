from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=50, default="")
    icon = models.ImageField(null=True)
    seller_count = models.PositiveIntegerField(default=0)
    visitor_count = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        db_table = 'core_wpservice_service'
