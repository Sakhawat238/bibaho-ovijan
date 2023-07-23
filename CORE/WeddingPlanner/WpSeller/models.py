from django.db import models
from AUTH.UserAuthentication.models import User


class Portfolio(models.Model):
    code = models.CharField(max_length=20,null=False,unique=True)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    picture = models.ImageField(null=True)
    bio = models.CharField(max_length=250, default="")
    details_info = models.TextField(default="")
    joining_date = models.DateField(auto_now_add=True)
    average_rating = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    is_archived = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.bio
    
    class Meta:
        db_table = 'core_wpseller_portfolio'
    

class ContactInfo(models.Model):
    portfolio = models.OneToOneField(Portfolio, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15, default="")
    email = models.CharField(max_length=100, default="")
    address = models.CharField(max_length=250, default="")
    website = models.CharField(max_length=50, default="")
    facebook = models.CharField(max_length=100, default="")
    instagram = models.CharField(max_length=100, default="")
    twitter = models.CharField(max_length=100, default="")
    behance = models.CharField(max_length=100, default="")
    whatsapp = models.CharField(max_length=100, default="")
    telegram = models.CharField(max_length=100, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.mobile
    
    class Meta:
        db_table = 'core_wpseller_contactinfo'
        

class RecentWork(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, default="")
    description = models.TextField(default="")
    picture = models.ImageField(null=True)
    date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        db_table = 'core_wpseller_recentwork'


class Tag(models.Model):
    title = models.CharField(max_length=100, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        db_table = 'core_wpseller_tag'

    
class SellerTag(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.portfolio.code
    
    class Meta:
        db_table = 'core_wpseller_sellertag'