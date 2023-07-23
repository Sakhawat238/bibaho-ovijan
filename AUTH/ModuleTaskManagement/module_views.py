from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from AUTH.LogWithAudit.views import audit_update
from AUTH.ModuleTaskManagement.models import Module, SubModule
from AUTH.utils import view_permission_required, DetailPermissions, UserCustomNav


@view_permission_required
def ModuleManagement(request, task_name="Module Management", action="main"):
    sub_modules = SubModule.objects.all().order_by('order')
    paginator = Paginator(sub_modules, 100)
    page = request.GET.get('page')
    paginated_sub_modules = paginator.get_page(page)
    context = {
        'sub_modules': paginated_sub_modules,
        'cnav': UserCustomNav(request, 'Authorization'),
        'privilege': DetailPermissions(request, 'Module Management')
    }
    return render(request, 'AUTH/ModuleTaskManagement/ModuleManagement.html', context)


@view_permission_required
def ModuleCreate(request, task_name="Module Management", action="add"):
    if request.method == 'POST':
        r = request.POST
        name = r.get('module_name')
        order = r.get('module_order')
        module_parent = r.get('module_parent')
        mtype = r.get('element_type')
        module_type = ''
        if mtype == 'c':
            module_type = 'configuration'
        elif mtype == 'o':
            module_type = 'operation'
        elif mtype == 'r':
            module_type = 'report'

        if SubModule.objects.filter(order=order).exists():
            messages.warning(request, f'Module order must be unique')
            return redirect('ModuleCreate')
        M = SubModule(name=name, order=order,
                      module_type=module_type, module_id=module_parent)
        M.save()

        audit_update(request, "Create", "SubModule", "ModuleCreate", "created a module", name)

        messages.success(request, f'Role updated successfully')

        messages.success(request, f'Module created successfully')
        return redirect('ModuleManagement')
    else:
        context = {
            'modules': Module.objects.all(),
            'cnav': UserCustomNav(request, 'Authorization'),
        }
        return render(request, 'AUTH/ModuleTaskManagement/ModuleCreate.html', context)


@view_permission_required
def ModuleEdit(request, id, task_name="Module Management", action="edit"):
    if request.method == 'POST':
        r = request.POST
        name = r.get('element_name')
        order = r.get('element_order')
        module_parent = r.get('module_parent')
        mtype = r.get('element_type')
        module_type = ''
        if mtype == 'c':
            module_type = 'configuration'
        elif mtype == 'o':
            module_type = 'operation'
        elif mtype == 'r':
            module_type = 'report'

        if SubModule.objects.filter(order=order).exclude(id=id).exists():
            messages.warning(request, f'Module order must be unique')
            return redirect('ModuleEdit', id=id)
        SubModule.objects.filter(id=id).update(
            name=name, order=order, module_type=module_type, module_id = module_parent)

        audit_update(request, "Edit", "SubModule", "ModuleEdit", "edited a module", name)

        messages.success(request, f'Module updated successfully')
        return redirect('ModuleManagement')
    else:
        sub_module = get_object_or_404(SubModule, id=id)
        context = {
            'sub_module': sub_module,
            'module': get_object_or_404(Module, id=sub_module.module_id),
            'modules': Module.objects.all(),
            'cnav': UserCustomNav(request, 'Authorization'),
        }
        return render(request, 'AUTH/ModuleTaskManagement/ModuleEdit.html', context)


@view_permission_required
def ModuleView(request, id, task_name="Module Management", action="view"):
    context = {
        'Module': get_object_or_404(SubModule, id=id),
        'cnav': UserCustomNav(request, 'Authorization'),
    }
    return render(request, 'AUTH/ModuleTaskManagement/ModuleView.html', context)
