from django.urls import path, include
from .views import LandingPage, Login, Logout


urlpatterns = [
    path('', LandingPage, name="LandingPage"),
    path('matrimony/', include('WEBSITE.Matrimony.urls')),
    path('wedding-planner/', include('WEBSITE.WeddingPlanner.urls')),
    path('login/', Login, name="WebsiteLogin"),
    path('logout/', Logout, name="WebsiteLogout")
]