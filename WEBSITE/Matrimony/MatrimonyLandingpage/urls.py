from django.urls import path
from .views import LandingPage

# ----- Ajax Services -----
from CORE.Common.Auth.services import sendOTP


urlpatterns = [
    path('', LandingPage, name="MatrimonyLandingPage"),


    #----- Ajax Calls -----
    path('ajax/send-otp', sendOTP, name="sendOTP")
]