from django.urls import path
from . import views

urlpatterns = [
    path('roles/',views.RoleAssignment,name='RoleManagement'),
    path('roles/add/',views.RoleCreate,name='RoleCreate'),
    path('roles/view/<int:id>/',views.RoleView,name='RoleView'),
    path('roles/edit/<int:id>/',views.RoleEdit,name='RoleEdit')
    
]
