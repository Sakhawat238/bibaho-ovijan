from django.urls import path
from .views import AddBookmark, BookmarkList


urlpatterns = [
    path('', BookmarkList, name="BookmarkList"),
    path('add/', AddBookmark, name="AddBookmark")
]