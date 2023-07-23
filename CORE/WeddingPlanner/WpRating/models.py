from django.db import models
from CORE.WeddingPlanner.WpSeller.models import Portfolio


class SellerRating(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.SET_NULL, null=True)
    rating = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    details = models.TextField(default="")
    service = models.CharField(max_length=50, default="")
    rated_by = models.CharField(max_length=100, default="")
    user_id = models.PositiveIntegerField(null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.rated_by
    
    class Meta:
        db_table = 'core_wprating_seller_rating'