from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from django.shortcuts import redirect
from django.core.cache import cache
from AUTH.TaskAssignment.models import UserWithTask, UserWithModule
from AUTH.ModuleTaskManagement.models import SubModule, Task
from AUTH.UserAuthentication.models import USER_TYPE
import sys

if sys.version_info[1] >= 11:
    from inspect import getfullargspec  
else:
    from inspect import getargspec

from bibahoovijan import settings


def module_permission_required(module_name):
    def _method_wrapper(function):
        @login_required(login_url=settings.ADMIN_LOGIN_URL)
        def _arguments_wrapper(request, *args, **kwargs):
            if UserWithModule.objects.filter(user_id=request.user.id,module__name=module_name).exists():
                return function(request, *args, **kwargs)
            else:
                return redirect('home_page')
        return _arguments_wrapper
    return _method_wrapper


def view_permission_required(function):
    @login_required(login_url=settings.ADMIN_LOGIN_URL)
    def wrap(request, *args, **kwargs):
        if sys.version_info[1] >= 11:
            argspec = getfullargspec(function)
        else:
            argspec = getargspec(function)
        task_name = argspec.defaults[0]
        task_action = argspec.defaults[1]
        current_user = request.user
        try:
            assigned_priv = UserWithTask.objects.get(task__name=task_name, user=current_user)
        except:
            messages.warning(request, f'you are not allowed to access this route')
            return redirect('home_page')
        if task_action == 'main' or getattr(assigned_priv,task_action+"_task"):
            return function(request, *args, **kwargs)
        else:
            messages.warning(request, f'you are not allowed to access this route')
            return redirect('home_page')     
    return wrap


def DetailPermissions(request, task_name):
    return UserWithTask.objects.get(task__name=task_name, user=request.user)


def UserCustomNav(request,module_name):
    requesteduser = request.user
    modules_dic = cache.get(requesteduser.username+'_'+module_name+'_cached_md')
    if modules_dic is None:
        modules_dic = {}
        assigned_tasks = requesteduser.userwithtask_set.all()
        all_modules = SubModule.objects.prefetch_related(
            Prefetch(
                'task_set',
                queryset=Task.objects.all().order_by('order'),
                to_attr='tasklist'
            )).filter(module__name=module_name).order_by('order')
        configuration = {}
        operation = {}
        report = {}
        has_config = False
        has_operation = False
        has_report = False
        for am in all_modules:
            tasks_under_module = am.tasklist
            if tasks_under_module:
                context_child_dic = {}
                count = 0
                for task in tasks_under_module:
                    for atask in assigned_tasks:
                        if atask.task_id == task.id:
                            new_dict = {
                                task.name : task.task_url
                            }
                            context_child_dic.update(new_dict)
                            count = count + 1
                if count != 0:
                    if am.module_type == 'configuration':
                        configuration.update({
                            am.name:context_child_dic
                        })
                        has_config = True
                    elif am.module_type == 'operation':
                        operation.update({
                            am.name:context_child_dic
                        })
                        has_operation = True
                    elif am.module_type == 'report':
                        report.update({
                            am.name:context_child_dic
                        })
                        has_report = True           
        if has_config:
            modules_dic.update({
                'configuration': configuration
            })
        if has_operation:
            modules_dic.update({
                'operation': operation
            })
        if has_report:
            modules_dic.update({
                'report': report
            })
        cache.set(requesteduser.username+'_cached_md', modules_dic, 300)
    return {
        'modules': modules_dic,
    }



def user_type_check(user_type=USER_TYPE.VISITOR, redirect_to=settings.VISITOR_LOGIN_URL):
    def wrapper(function):
        @login_required(login_url=redirect_to)
        def wrap(request, *args, **kwargs):
            if user_type and request.user.type == user_type:
                return function(request, *args, **kwargs)
            return redirect(redirect_to)
        return wrap
    return wrapper