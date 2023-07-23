from django.shortcuts import render, redirect
from django.contrib import messages
from CORE.Common.Auth.services import Login as LoginService, Logout as LogoutService

def LandingPage(request):
    context = {}
    return render(request, 'WEBSITE/LandingPage.html', context)


def Login(request):
    r = request.POST
    mobile = r.get('mobile_no')
    password = r.get('pass_word')
    success = LoginService(request, mobile, password)
    print(success)
    if success:
        messages.success(request, f'You have logged in successfully')
    else:
        messages.error(request, 'Logged in failed. Please try again.')
    return redirect("LandingPage")


def Logout(request):
    LogoutService(request)
    return redirect("LandingPage")