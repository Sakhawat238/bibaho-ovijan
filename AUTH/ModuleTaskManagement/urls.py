from django.urls import path
from . import module_views, task_views

urlpatterns = [
    # MODULE MANAGEMENT URLS
    path('modules/', module_views.ModuleManagement, name='ModuleManagement'),
    path('modules/create/', module_views.ModuleCreate, name='ModuleCreate'),
    path('modules/edit/<int:id>', module_views.ModuleEdit, name='ModuleEdit'),
    path('modules/view/<int:id>', module_views.ModuleView, name='ModuleView'),

    # TASK MANAGEMENT URLS
    path('tasks/', task_views.task_management, name='TaskManagement'),
    path('tasks/create/', task_views.task_create, name='TaskCreate'),
    path('tasks/edit/<int:id>', task_views.task_edit, name='TaskEdit'),
    path('tasks/view/<int:id>', task_views.task_view , name='TaskView'),
]
