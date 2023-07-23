from .models import Service
from django.db.models import F


def get_service_list():
    return Service.objects.all()

def get_service_list_min():
    return Service.objects.only('id','title')

def get_popular_services():
    return Service.objects.annotate(rating=F('seller_count')*1+F('visitor_count')*1.25).only('id','title').order_by('-rating')[:4]

def update_service_seller_count(id, inc):
    Service.objects.filter(id=id).update(seller_count=F('seller_count')+inc)