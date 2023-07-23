from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from AUTH.UserAuthentication.models import User, USER_TYPE
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q

import re

from .models import UserWithModule, UserWithRole, UserWithTask
from .forms import UserWithRoleForm
from AUTH.RoleCreation.models import Role, RoleDistribution
from AUTH.ModuleTaskManagement.models import Module, SubModule, Task
from AUTH.LogWithAudit.views import audit_update
from AUTH.utils import DetailPermissions, view_permission_required, UserCustomNav


def IsPasswordValid(password):
    if len(password) < 6:
        return False
    if not re.findall('\d', password):
        return False
    if not re.findall('[A-Z]', password):
        return False
    if not re.findall('[a-z]', password):
        return False
    if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
        return False
    return True


@view_permission_required
def TaskAssignment(request, task_name="User Management", action="main"):
    # if request.user.is_staff:
    #     users = UserWithRole.objects.select_related('user', 'role').all()
    # else:
    #     user_obj = get_object_or_404(UserWithRole, user=request.user)
    users = UserWithRole.objects.select_related('user', 'role').all()
    nameq = request.GET.get('username')
    if nameq:
        users = users.filter(user__username__icontains=nameq)
    users = users.order_by('user__username')
    paginator = Paginator(users, 20)
    page = request.GET.get('page')
    user_list = paginator.get_page(page)
    llist = []
    for u in user_list:
        llist.append({
            'id': u.id,
            'username': u.user.username,
            'fullname': u.user.first_name,
            'shortname': u.user.last_name,
            'mobile': u.mobile,
            'email': u.user.email,
            'role': u.role.name
        })
    main_context = {
        'users': user_list,
        'context': llist,
        'privilege': DetailPermissions(request, 'User Management'),
        'cnav': UserCustomNav(request, 'Authorization'),

    }
    return render(request, 'AUTH/TaskAssignment/RoleAssignment.html', main_context)


@view_permission_required
def NewRoleAssign(request, task_name="User Management", action="add"):
    if request.method == 'POST':
        r = request.POST
        with transaction.atomic():
            try:
                u_name = r.get('userName')
                p_word = r.get('password')
                c_p_word = r.get('confirmpassword')
                email = r.get('useremail')
                full_name = r.get('fullname')
                mobile_no = r.get('mobileno')
                role_list = r.get('roleselect')
                if u_name == "" or p_word == "" or email == "" or full_name == "" or mobile_no == "":
                    messages.warning(request, f'Please provide required information.')
                    return redirect('NewRoleAssign')
                if p_word != c_p_word:
                    messages.warning(request, f'Password did not match.')

                    return redirect('NewRoleAssign')
                if not IsPasswordValid(p_word):
                    messages.warning(request,
                                     f'Password length should be minimum 6 and must contain minimum 1 uppercase letter, 1 lowercase letter, 1 number and 1 symbol.')
                    return redirect('NewRoleAssign')
                if User.objects.filter(Q(username=u_name) | Q(email=email)).exists():
                    messages.warning(request, f'username or email already exists !')
                    return redirect('NewRoleAssign')
                if UserWithRole.objects.filter(mobile=mobile_no).exists():
                    messages.warning(request, f'Mobile number already exists !')
                    return redirect('NewRoleAssign')
                made_password = make_password(p_word)
                UserObj = User(username=u_name, first_name=full_name, email=email, password=made_password,
                               type=USER_TYPE.ADMIN)
                UserObj.save()
                U = UserWithRole(user=UserObj, mobile=mobile_no, role=Role.objects.filter(id=role_list).first())
                U.save()
                form = UserWithRoleForm(request.POST, request.FILES, instance=U)
                if form.is_valid:
                    form.save()
                selected_roles = RoleDistribution.objects.filter(role=role_list)
                modules = set()
                selected_modules = []
                for sr in selected_roles:
                    temp = UserWithTask()
                    temp.user = UserObj
                    temp.task = sr.task
                    temp.view_task = sr.view_task
                    temp.add_task = sr.add_task
                    temp.save_task = sr.save_task
                    temp.edit_task = sr.edit_task
                    temp.delete_task = sr.delete_task
                    temp.print_task = sr.print_task
                    temp.cancel_task = sr.cancel_task
                    temp.reset_task = sr.reset_task
                    temp.find_task = sr.find_task
                    temp.save()
                    modules.add(sr.task.module.module_id)
                for i in modules:
                    selected_modules.append(UserWithModule(user=UserObj, module_id=i))
                UserWithModule.objects.bulk_create(selected_modules, batch_size=50)

                c_data = 'Username: ' + u_name
                audit_update(request, "Create", "User, UserWithModule, UserWithTask", "UserCreate", "created a new user with username: " + u_name, c_data)

                messages.success(request, f'User created successfully')
            except Exception as e:
                print(repr(e))
                messages.success(request, f'{e}')

        return redirect('TaskAssignment')
    else:
        if request.user.is_staff:
            all_roles = Role.objects.exclude(name__in=['Developer'])
        elif request.user.is_superuser:
            all_roles = Role.objects.exclude(name__in=['Superadmin', 'Developer'])
        else:
            all_roles = Role.objects.exclude(name__in=['Superadmin', 'Developer', 'Company admin', 'Technical admin'])
            user_obj = get_object_or_404(UserWithRole, user=request.user)
        context = {
            'roles': all_roles,
            'form': UserWithRoleForm(),
            'cnav': UserCustomNav(request, 'Authorization'),

        }
        return render(request, 'AUTH/TaskAssignment/RoleAssignmentCreate.html', context)


@view_permission_required
def View(request, id, task_name="User Management", action="view"):
    u = UserWithRole.objects.select_related('user').filter(id=id).first()
    context = {
        'userwithrole': u,
        'userObj': u.user,
        'cnav': UserCustomNav(request, 'Authorization'),
    }
    return render(request, 'AUTH/TaskAssignment/RoleAssignmentView.html', context)


@view_permission_required
def Edit(request, id, task_name="User Management", action="edit"):
    userwithrole = get_object_or_404(UserWithRole, id=id)
    if not request.user.is_superuser:
        if userwithrole.role.name == 'company admin':
            messages.warning(request, 'You can not edit this user')
            return redirect('TaskAssignment')
    if request.method == 'POST':
        with transaction.atomic():
            try:
                r = request.POST
                u_name = r.get('username')
                full_name = r.get('fullname')
                p_word = r.get('password')
                c_p_word = r.get('confirmpassword')
                email = r.get('useremail')
                mobile_no = r.get('mobileno')
                role_list = r.get('roleselect')
                if u_name == "" or email == "" or full_name == "" or mobile_no == "":
                    messages.warning(request, f'Please provide required information.')
                    return redirect('RoleAssignmentEdit', id=id)
                if p_word != '':
                    if p_word != c_p_word:
                        messages.warning(request, f'Password did not match.')
                        return redirect('RoleAssignmentEdit', id=id)
                    if not IsPasswordValid(p_word):
                        messages.warning(request,
                                         f'Password length should be minimum 6 and must contain minimum 1 uppercase letter, 1 lowercase letter, 1 number and 1 symbol.')
                        return redirect('RoleAssignmentEdit', id=id)
                user_obj = userwithrole.user
                if u_name != user_obj.username and User.objects.filter(username=u_name).exists():
                    messages.warning(request, f'username already exists !')
                    return redirect('RoleAssignmentEdit', id=id)
                if email != user_obj.email and User.objects.filter(email=email).exists():
                    messages.warning(request, f'email already exists !')
                    return redirect('RoleAssignmentEdit', id=id)
                if mobile_no != userwithrole.mobile and UserWithRole.objects.filter(mobile=mobile_no).exists():
                    messages.warning(request, f'Mobile number already exists !')
                    return redirect('RoleAssignmentEdit', id=id)

                prevusername = user_obj.username
                user_obj.username = u_name
                user_obj.first_name = full_name
                user_obj.email = email
                if p_word != '':
                    made_password = make_password(p_word)
                    user_obj.password = made_password
                user_obj.save()
                userwithrole.mobile = mobile_no
                p_form = UserWithRoleForm(request.POST, request.FILES, instance=userwithrole)
                if p_form.is_valid:
                    p_form.save()
                userwithrole.save()

                # selected_roles = RoleDistribution.objects.filter(role=role_list)
                #
                # for obj in UserWithTask.objects.all():
                #     if obj.user.id == userwithrole.user.id:
                #         obj.delete()
                #
                # for sr in selected_roles:
                #     temp = UserWithTask()
                #
                #     temp.user = user_obj
                #     temp.task = sr.task
                #     temp.view_task = sr.view_task
                #     temp.add_task = sr.add_task
                #     temp.save_task = sr.save_task
                #     temp.edit_task = sr.edit_task
                #     temp.delete_task = sr.delete_task
                #     temp.print_task = sr.print_task
                #     temp.cancel_task = sr.cancel_task
                #     temp.reset_task = sr.reset_task
                #     temp.find_task = sr.find_task
                #     temp.save()

                audit_update(request, "Edit", "User, UserWithRole, UserWithModule", "UserEdit", "updated user: " + prevusername,"")

                messages.success(request, f'User edited successfully')
            except Exception as e:
                print(repr(e))
                messages.warning(request, f'{e}')

        return redirect('TaskAssignment')
    else:
        if request.user.is_staff:
            all_roles = Role.objects.exclude(name__in=['Developer'])
        elif request.user.is_superuser:
            all_roles = Role.objects.exclude(name__in=['Superadmin', 'Developer'])
        else:
            all_roles = Role.objects.exclude(name__in=['Superadmin', 'Developer', 'Company admin', 'Technical admin'])
        user_obj = userwithrole.user
        context = {
            'userwithrole': userwithrole,
            'userObj': user_obj,
            'all_roles': all_roles,
            'p_form': UserWithRoleForm(instance=userwithrole),
            'cnav': UserCustomNav(request, 'Authorization'),

        }
        return render(request, 'AUTH/TaskAssignment/RoleAssignmentEdit.html', context)


@view_permission_required
def Delete(request, id, task_name="User Management", action="delete"):
    return redirect('TaskAssignment')


@view_permission_required
def UpdateUserPermission(request, id, task_name="User Management", action="cancel"):
    if request.method == 'POST':
        with transaction.atomic():
            try:
                all_tasks = Task.objects.select_related('module').all()
                userwithrole = get_object_or_404(UserWithRole, id=id)
                userid = userwithrole.user_id
                r = request.POST
                selected_modules = set()
                # for am in all_modules:
                #     task_under_module = am.task_set.all().order_by('order')
                #     for tum in task_under_module:
                #         available_task_list.append({
                #             'task': tum,
                #             'moduleid': am.module_id
                #         })
                for t in all_tasks:
                    Task_list = r.getlist(t.name + '_element_task')
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
                    if view_T or add_T or save_T or edit_T or delete_T or cancel_T or print_T or reset_T or find_T:
                        selected_modules.add(t.module.module_id)
                        obj, created = UserWithTask.objects.update_or_create(user_id=userid, task=t,
                                                                             defaults={"view_task": view_T,
                                                                                       "add_task": add_T,
                                                                                       "save_task": save_T,
                                                                                       "edit_task": edit_T,
                                                                                       "delete_task": delete_T,
                                                                                       "print_task": print_T,
                                                                                       "cancel_task": cancel_T,
                                                                                       "reset_task": reset_T,
                                                                                       "find_task": find_T})
                    else:
                        UserWithTask.objects.filter(user_id=userid, task=t).delete()
                UserWithModule.objects.filter(user_id=userid).delete()
                user_modules = []
                for sm in selected_modules:
                    user_modules.append(UserWithModule(user_id=userid, module_id=sm))
                UserWithModule.objects.bulk_create(user_modules, batch_size=50)

                audit_update(request, "Edit", "UserWithTask", "UpdateUserPermission", "updated user permissions", "")

                messages.success(request, f'Permissions updated successfully')
            except Exception as e:
                repr(e)
                messages.warning(request, f'{e}')

        return redirect('TaskAssignment')
    else:
        # developer_status = request.user.is_staff
        # if developer_status:
        all_modules = SubModule.objects.all().order_by('order')
        all_tasks = Task.objects.all()
        # else:
        #     all_modules = SubModule.objects.all().exclude(name__in=["Module Management", "Company Management"]).order_by(
        #         'order')
        #     all_tasks = Task.objects.all().exclude(name='Role Management')
        userwithrole = get_object_or_404(UserWithRole, id=id)
        user_tasks = UserWithTask.objects.filter(user_id=userwithrole.user_id)
        task_list = []
        for atask in all_tasks:
            T = {
                'taskName': atask.name,
                'moduleId': atask.module_id,
                'view': atask.view_task,
                'view_c': 0,
                'add': atask.add_task,
                'add_c': 0,
                'save': atask.save_task,
                'save_c': 0,
                'edit': atask.edit_task,
                'edit_c': 0,
                'delete': atask.delete_task,
                'delete_c': 0,
                'print': atask.print_task,
                'print_c': 0,
                'cancel': atask.cancel_task,
                'cancel_c': 0,
                'reset': atask.reset_task,
                'reset_c': 0,
                'find': atask.find_task,
                'find_c': 0,
            }
            task_list.append(T)
        for x in task_list:
            for y in user_tasks:
                if x['taskName'] == y.task.name:
                    x['view_c'] = 0 | y.view_task
                    x['add_c'] = 0 | y.add_task
                    x['save_c'] = 0 | y.save_task
                    x['edit_c'] = 0 | y.edit_task
                    x['delete_c'] = 0 | y.delete_task
                    x['print_c'] = 0 | y.print_task
                    x['cancel_c'] = 0 | y.cancel_task
                    x['reset_c'] = 0 | y.reset_task
                    x['find_c'] = 0 | y.find_task
        context = {
            # 'cnav': UserCustomNav(request),
            'mdls': all_modules,
            'task_list': task_list,
            'user_name': userwithrole.user.first_name,
            'cnav': UserCustomNav(request, 'Authorization'),

        }
        return render(request, 'AUTH/TaskAssignment/UpdateUserPermission.html', context)
