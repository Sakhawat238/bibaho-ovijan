from django.http import JsonResponse
from AUTH.TaskAssignment.models import UserWithModule, UserWithRole
from AUTH.ModuleTaskManagement.models import Module
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout, authenticate, login
from AUTH.UserAuthentication.models import USER_TYPE

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from AUTH.TaskAssignment.views import IsPasswordValid
from AUTH.utils import user_type_check
from bibahoovijan import settings


def login_view(request):
    if request.method == 'POST':
        r = request.POST
        username = r.get('username')
        password = r.get('password')
        rurl = r.get('rurl')
        redirect_url = 'home_page'
        if rurl:
            redirect_url = rurl
        user = authenticate(request, username=username, password=password)
        if user is not None and user.type != USER_TYPE.VISITOR:
            messages.success(request, f'Welcome Back !')
            login(request, user)
            return redirect(redirect_url)
        else:
            messages.error(request, f'Invalid credentials !')
            return redirect('loginpage')
    else:
        ru = request.GET.get('next')
        if ru:
            nexturl = ru
        else:
            nexturl = ''
        return render(request, 'AUTH/UserAuth/login.html', {'next': nexturl})


@user_type_check(USER_TYPE.ADMIN, redirect_to=settings.ADMIN_LOGIN_URL)
def home_page(request):
    userid = request.user.id
    usermodules = UserWithModule.objects.filter(user_id=userid).values('module_id')
    modules = Module.objects.filter(id__in=usermodules).order_by('order')
    context = {
        'modules': modules,
    }
    return render(request, 'AUTH/UserAuth/home.html', context)


@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        r = request.POST
        current_password = r.get('current_password')
        new_password = r.get('new_password')
        confirm_new_password = r.get('confirm_new_password')

        if confirm_new_password != new_password:
            messages.warning(request, f'Please confirm your password correctly')
            return redirect('profile')

        if not IsPasswordValid(new_password):
            messages.warning(request,
                             f'Password length should be minimum 6 and must contain minimum 1 uppercase letter, 1 lowercase letter, 1 number and 1 symbol.')
            return redirect('profile')

        if user.check_password(current_password):
            user.set_password(new_password)
            user.save()

        messages.warning(request, f'Your profile successfully updated!')
        return redirect('profile')
    else:
        extended_user = UserWithRole.objects.select_related('user').get(user=user)
        context = {
            'extended_user': extended_user
        }
        return render(request, 'AUTH/UserAuth/user.profile.html', context)


@login_required
def profile_photo_upload(request):
    r = request.POST
    user_id = r.get('user_id')
    try:
        user = get_object_or_404(UserWithRole, user_id=user_id)
        user.picture = request.FILES.get('profile-photo')
        user.save()

        return JsonResponse({
            'success': True,
            'src': user.picture.url
        })
    except:
        return JsonResponse({
            'success': False
        })


@login_required
def logout_view(request):
    messages.info(request, f'You are successfully logged out...')
    logout(request)
    return redirect('loginpage')
