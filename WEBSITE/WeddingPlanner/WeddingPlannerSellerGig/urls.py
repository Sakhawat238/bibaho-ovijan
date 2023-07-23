from django.urls import path
from .views import GigAdd, GigList, GigView, GigEdit


urlpatterns = [
    path('add/', GigAdd, name="SellerGigAdd"),
    path('list', GigList, name="SellerGigList"),
    path('view/<int:id>/', GigView, name="SellerGigView"),
    path('edit/<int:id>/<str:slug>/', GigEdit, name="SellerGigEdit")
]
