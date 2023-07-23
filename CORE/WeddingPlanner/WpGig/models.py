from django.db import models
from CORE.WeddingPlanner.WpSeller.models import Portfolio
from CORE.WeddingPlanner.WpService.models import Service
from CORE.utils import generate_unique_id_fixed_length_v1


class PackageType(models.TextChoices):
    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"
    CUSTOM = "Custom"

def upload_location(instance, filename):
    extension = filename.split(".")[1]
    changed_file_name = generate_unique_id_fixed_length_v1(15)
    return "%s.%s" % (changed_file_name, extension)


class Gig(models.Model):
    title = models.CharField(max_length=250, default="")
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    service_type = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    location = models.CharField(max_length=50, default="Anywhere")
    description = models.TextField(default="")
    thumbnail = models.ImageField(upload_to=upload_location, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        db_table = 'core_wpgig_gig'


class Gallary(models.Model):
    gig = models.ForeignKey(Gig, on_delete=models.CASCADE)
    file = models.FileField(upload_to=upload_location, null=True) # Filefield bcoz we will allow pdf file in later version
    created_at = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.gig.title
    
    class Meta:
        db_table = 'core_wpgig_gallary'


class Package(models.Model):
    gig = models.ForeignKey(Gig, on_delete=models.CASCADE)
    category = models.CharField(max_length=15, choices=PackageType.choices, default=PackageType.STANDARD)
    description = models.TextField(default="")
    price = models.CharField(max_length=50, default="")
    show_price = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.gig.title
    
    class Meta:
        db_table = 'core_wpgig_package'


class SellerFaq(models.Model):
    gig = models.ForeignKey(Gig, on_delete=models.CASCADE)
    question = models.CharField(max_length=250, default="")
    answer = models.CharField(max_length=500, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.gig.title
    
    class Meta:
        db_table = 'core_wpgig_sellerfaq'


# class BuyerFaq(models.Model):
#     We will implement this feature on later version
#     A set of quetsion that will be answered by the buyer
#     like, when will the event happen, how much budget they have etc
