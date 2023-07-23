from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Module, SubModule, Task
from AUTH.utils import DetailPermissions, view_permission_required, UserCustomNav
from AUTH.LogWithAudit.views import audit_update


@view_permission_required
def task_management(request, task_name="Task Management", action="main"):
    all_tasks = Task.objects.select_related('module').all().order_by('order')
    paginator = Paginator(all_tasks, 20)
    page = request.GET.get('page')
    tasks = paginator.get_page(page)
    context = {
        'Tsks': tasks,
        'privilege': DetailPermissions(request, 'Task Management'),
        'cnav': UserCustomNav(request, 'Authorization'),
    }
    return render(request, 'AUTH/ModuleTaskManagement/TaskManagement.html', context)


@login_required
@view_permission_required
def task_view(request, id, task_name='Task Management', action='view'):
    context = {
        'Task': get_object_or_404(Task, id=id),
        'cnav': UserCustomNav(request, 'Authorization'),
    }
    return render(request, 'AUTH/ModuleTaskManagement/TaskView.html', context)
    

@view_permission_required
def task_create(request, task_name='Task Management', action='add'):
    if request.method == 'POST':
        r = request.POST
        name = r.get('element_name')
        order = r.get('element_order')
        moduleId = r.get('element_module')
        if Task.objects.filter(name=name).exists():
            messages.warning(request, f'Task name already exists.')
            return redirect('TaskCreate')
        if Task.objects.filter(order=order).exists():
            messages.warning(request, f'Task order already exists.')
            return redirect('TaskCreate')
        url = r.get('task_url')
        Task_list = r.getlist('element_event')
        view_T = 0
        add_T = 0
        save_T = 0
        edit_T = 0
        delete_T = 0
        print_T = 0
        cancel_T = 0
        reset_T = 0
        find_T = 0
        if 'view_checked' in Task_list:
            view_T = 1
        if 'add_checked' in Task_list:
            add_T = 1
        if 'save_checked' in Task_list:
            save_T = 1
        if 'edit_checked' in Task_list:
            edit_T = 1
        if 'delete_checked' in Task_list:
            delete_T = 1
        if 'print_checked' in Task_list:
            print_T = 1
        if 'cancel_checked' in Task_list:
            cancel_T = 1
        if 'reset_checked' in Task_list:
            reset_T = 1
        if 'find_checked' in Task_list:
            find_T = 1
        T = Task(name=name, order=order, module_id=moduleId, task_url=url, view_task=view_T,
                 add_task=add_T, save_task=save_T, edit_task=edit_T, delete_task=delete_T,
                 print_task=print_T, cancel_task=cancel_T, reset_task=reset_T, find_task=find_T)
        T.save()

        audit_update(request, "Create", "Task", "TaskCreated", "created a task", name)

        messages.success(request, f'Task created successfully.')
        return redirect('TaskManagement')
    else:
        context = {
            'mdls': SubModule.objects.all(),
            'cnav': UserCustomNav(request, 'Authorization'),
           
        }
        return render(request, 'AUTH/ModuleTaskManagement/TaskCreate.html', context)


@view_permission_required
def task_edit(request, id, task_name="Task Management", action="edit"):
    if request.method == 'POST':
        r = request.POST
        name = r.get('element_name')
        order = r.get('element_order')
        moduleId = r.get('element_module')
        if Task.objects.filter(name=name).exclude(id=id).exists():
            messages.warning(request, f'Task name already exists.')
            return redirect('TaskEdit', id=id)
        if Task.objects.filter(order=order).exclude(id=id).exists():
            messages.warning(request, f'Task order already exists.')
            return redirect('TaskEdit', id=id)
        url = r.get('task_url')
        Task_list = r.getlist('element_task')
        view_T = 0
        add_T = 0
        save_T = 0
        edit_T = 0
        delete_T = 0
        print_T = 0
        cancel_T = 0
        reset_T = 0
        find_T = 0
        if 'view_checked' in Task_list:
            view_T = 1
        if 'add_checked' in Task_list:
            add_T = 1
        if 'save_checked' in Task_list:
            save_T = 1
        if 'edit_checked' in Task_list:
            edit_T = 1
        if 'delete_checked' in Task_list:
            delete_T = 1
        if 'print_checked' in Task_list:
            print_T = 1
        if 'cancel_checked' in Task_list:
            cancel_T = 1
        if 'reset_checked' in Task_list:
            reset_T = 1
        if 'find_checked' in Task_list:
            find_T = 1
        Task.objects.filter(id=id).update(name=name, order=order, module_id=moduleId, task_url=url,
                                          view_task=view_T, add_task=add_T, save_task=save_T, edit_task=edit_T,
                                          delete_task=delete_T,
                                          print_task=print_T, cancel_task=cancel_T, reset_task=reset_T,
                                          find_task=find_T)

        audit_update(request, "Edit", "Task", "TaskEdit", "edited a task", name)

        messages.success(request, f'Task updated successfully.')
        return redirect('TaskManagement')
    else:
        task = get_object_or_404(Task, id=id)
        context = {
            'task': task,
            'mdls': SubModule.objects.all(),
            'cnav': UserCustomNav(request, 'Authorization'),
           
        }
        return render(request, 'AUTH/ModuleTaskManagement/TaskEdit.html', context)
