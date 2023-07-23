from django.urls import path
from .views import login_view, logout_view, home_page, profile, profile_photo_upload
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='login/')),
    path('login/', login_view, name="loginpage"),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='profile'),
    path('home/', home_page, name="home_page"),
    path('profile-photo/upload', profile_photo_upload, name="profile_photo_upload"),
    # path('profile/', views.UpdateProfile, name="userprofile"),
]
