


from django.urls import path
from . import views

urlpatterns = [
    path('', views.AuthDashboard, name="AuthDashboardV1")
]