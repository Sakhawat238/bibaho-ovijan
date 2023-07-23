from django.urls import path
from .views import (WeddingPlanChecklist, WeddingPlanNote, WeddingPlanDirectory, AddWeddingPlanChecklist,
                    MarkWeddingPlanChecklistComplete, DeleteWeddingPlanChecklist, AddWeddingPlanNote, AddWeddingPlanDirectory)


urlpatterns = [
    path('checklists/', WeddingPlanChecklist, name="WeddingPlanChecklist"),
    path('checklists/add/', AddWeddingPlanChecklist, name="AddWeddingPlanChecklist"),
    path('checklists/update/<int:id>/', MarkWeddingPlanChecklistComplete, name="MarkWeddingPlanChecklistComplete"),
    path('checklists/delete/<int:id>/', DeleteWeddingPlanChecklist, name="DeleteWeddingPlanChecklist"),
    path('notes/', WeddingPlanNote, name="WeddingPlanNote"),
    path('notes/add/', AddWeddingPlanNote, name="AddWeddingPlanNote"),
    path('directory/', WeddingPlanDirectory, name="WeddingPlanDirectory"),
    path('directory/add/', AddWeddingPlanDirectory, name="AddWeddingPlanDirectory")
]