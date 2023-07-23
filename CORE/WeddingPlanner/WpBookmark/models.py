from django.db import models
from AUTH.UserAuthentication.models import User
from CORE.WeddingPlanner.WpSeller.models import Portfolio
from CORE.WeddingPlanner.WpGig.models import Gig



class BookmarkSeller(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seller = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    remarks = models.CharField(max_length=250, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.first_name
    
    class Meta:
        db_table = 'core_wpbookmark_seller'


class BookmarkGig(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gig = models.ForeignKey(Gig, on_delete=models.CASCADE)
    remarks = models.CharField(max_length=250, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.first_name
    
    class Meta:
        db_table = 'core_wpbookmark_gig'
