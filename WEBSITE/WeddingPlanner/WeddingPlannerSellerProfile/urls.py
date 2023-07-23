from django.urls import path
from .views import SellerProfile, SellerProfilePublicView, SellerProfileEdit, AddRecentWork


urlpatterns = [
    path('<str:slug>/', SellerProfile, name="SellerProfile"),
    path('<str:slug>/edit/', SellerProfileEdit, name="SellerProfileEdit"),
    path('public/<str:slug>/', SellerProfilePublicView, name="SellerProfilePublicView"),
    path('recent-works/add/', AddRecentWork, name="SellerProfileAddRecentWork"),
]
