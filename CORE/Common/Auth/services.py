from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.hashers import make_password
from bibahoovijan import settings
from AUTH.UserAuthentication.models import User, USER_TYPE
from .models import OTP
from CORE.utils import getCommonResponse, getCommonResponse
from CORE.WeddingPlanner.WpSeller.services import CreateInitialProfile
from datetime import datetime, timedelta
import re


def check_mobile_email_validity(mobile, email):
    email_valid = True
    mobile_valid = True

    if User.objects.filter(email=email).exists():
        email_valid = False

    if User.objects.filter(mobile=mobile).exists():
        mobile_valid = False

    return {
        'email': email_valid,
        'mobile': mobile_valid
    }


def sendOTP(request):
    mobile = request.POST.get('mobile')
    if re.search("01[3-9]{1}[0-9]{8}", mobile):
        mobile = "01"+mobile.split('01')[1]

        otpcode = 123456 # 6 digit OTP
        otp, created = OTP.objects.get_or_create(contact=mobile, is_mobile=True, defaults={'resend_count': 0, 'code': int(otpcode)})

        if not created: # Resend
            if otp.resend_count == settings.MOBILE_OTP_VERIFICATION_RESEND_LIMIT:
                return getCommonResponse(False, "OTP limit finished")
            else:
                otp.code = otpcode
                otp.resend_count += 1
                otp.timestamp = datetime.now()
                otp.save()
        
        # send_sms()
        print('--------- SMS Sent ----------')

        return getCommonResponse(True, "OTP sent.")
    else:
        return getCommonResponse(False, "OTP sent failed.")

@csrf_exempt
def registerUser(request):        
    r = request.POST
    
    fullname = r.get('fullname')
    email = r.get('email')
    mobile = r.get('mobile')
    password = r.get('password')
    otpcode = r.get('otp')

    if fullname == "" or email == "" or mobile == "" or password == "" or otpcode == "":
        return getCommonResponse(False, "All data are required.")
    try:
        if User.objects.filter(username=mobile, mobile=mobile).exists():
            return getCommonResponse(False, "Mobile already used.")

        otp = OTP.objects.get(contact = mobile, code = otpcode)
        dif = int(((datetime.now() - (otp.timestamp.replace(tzinfo=None)+ timedelta(hours=6))).total_seconds())/60)
        if dif > settings.MOBILE_OTP_VERIFICATION_VALIDITY_MINUTES:
            return getCommonResponse(False, "OTP Expired.")

    except:
        pass
    


    made_password = make_password(password)
    UserObj = User(username=mobile, first_name=fullname, email=email, password=made_password, mobile=mobile, mobile_verified = True, type=USER_TYPE.VISITOR)
    UserObj.save()
    
    return getCommonResponse(True, "Successfull")


# @csrf_exempt
# def Login(request):        
#     r = request.POST
    
#     email = r.get('email')
#     password = r.get('password')

#     if email == "" or password == "":
#         return getCommonResponse(False, "All data are required.")
    
#     user = authenticate(request, username=email, password=password)
#     if user:
#         login(request, user)
#         return getCommonResponse(True, "Login Successful.")

#     return getCommonResponse(False, "Login Failed.")


def CreateSellerAccount(fullname,mobile,email,password):
    try:
        made_password = make_password(password)
        UserObj = User(username=mobile, first_name=fullname, last_name=fullname, 
                    email=email, password=made_password, mobile=mobile, mobile_verified=True, 
                    type=USER_TYPE.SELLER)
        UserObj.save()
    except:
        return False
    
    try:
        CreateInitialProfile(mobile, email, UserObj.id)
    except:
        UserObj.delete()
        return False
    
    return True
    

def Login(request, username, password):
    if username and password:
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return True
    return False


def Logout(request):
    logout(request)