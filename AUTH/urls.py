from django.urls import path, include

urlpatterns = [
    path('', include('AUTH.UserAuthentication.urls')),

    path('dashboard/', include('AUTH.AuthDashboard.urls')),

    path('module-management/', include('AUTH.ModuleTaskManagement.urls')),

    path('role-management/', include('AUTH.RoleCreation.urls')),

    path('user-management/', include('AUTH.TaskAssignment.urls')),

    path('task-assignment/', include('AUTH.TaskAssignment.urls')),
    
    path('audit/', include('AUTH.LogWithAudit.urls')),
]