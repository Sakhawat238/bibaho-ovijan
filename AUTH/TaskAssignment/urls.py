from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.TaskAssignment, name='TaskAssignment'),
    path('users/add/', views.NewRoleAssign, name='NewRoleAssign'),
    path('users/edit/<int:id>', views.Edit, name='RoleAssignmentEdit'),
    path('users/view/<int:id>', views.View, name='RoleAssignmentView'),
    path('users/delete/<int:id>', views.Delete, name='RoleAssignmentDelete'),
    path('users-update-role/<int:id>/', views.UpdateUserPermission, name="UpdateUserPermission"),

    # path('ajax-load-csn/', views.load_company_short_name, name="ajaxLoadCsn")
]
