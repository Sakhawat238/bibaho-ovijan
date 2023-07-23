from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from CORE.Common.Auth.services import check_mobile_email_validity, CreateSellerAccount, Login
from CORE.WeddingPlanner.WpService.services import get_service_list_min, get_service_list, get_popular_services


def LandingPage(request):
    context = {
        'loggedin': not request.user.is_anonymous,
        'service_names': get_service_list_min(),
        'service_list': get_service_list(),
        'popular_services': get_popular_services()
    }
    return render(request, 'WEBSITE/WeddingPlanner/LandingPage.html', context)



def RegisterSeller(request):
    r = request.POST
    fullname = r.get('full_name')
    mobile = r.get('mobile_no')
    email = r.get('email_address')
    password = r.get('pass_word')

    success = CreateSellerAccount(fullname, mobile, email, password)
    print(success)
    if success:
        Login(request, mobile, password)
        messages.success(request, f'Your account has been created successfully')
        return redirect("WeddingPlannerLandingPage")
    else:
        messages.error(request, 'Account creation failed. Please try again.')
        return redirect("WeddingPlannerLandingPage")
    

def check_valid_mobile_email(request):
    r = request.GET
    m = r.get('mobile')
    e = r.get('email')
    res = check_mobile_email_validity(m,e)
    return JsonResponse(res)