from django.urls import path
from .views import LandingPage, RegisterSeller, check_valid_mobile_email


urlpatterns = [
    path('', LandingPage, name="WeddingPlannerLandingPage"),
    path('seller-register/', RegisterSeller, name="RegisterSeller"),
    #ajax call
    path('api/check-mobile-email/', check_valid_mobile_email, name="apicheckvalidmobileemail")
]