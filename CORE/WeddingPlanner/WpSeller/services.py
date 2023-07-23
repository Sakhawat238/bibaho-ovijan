from AUTH.UserAuthentication.models import User
from .models import Portfolio, ContactInfo, RecentWork
from .utils import generate_seller_code
from CORE.utils import change_file_name, file_upload_server


def CreateInitialProfile(mobile, email, userid):
    code = generate_seller_code()
    P = Portfolio(code=code, user_id=userid)
    P.save()
    C = ContactInfo(portfolio_id=P.id, mobile=mobile, email=email)
    C.save()


def GetProfileData(slug):
    try:
        U = User.objects.get(slug=slug)
        P = Portfolio.objects.get(user_id=U.id)
        C = ContactInfo.objects.get(portfolio_id=P.id)

        profile_completion = 0
        if U.mobile_verified:
            profile_completion = profile_completion + 10
        if U.email_verified:
            profile_completion = profile_completion + 10
        if U.last_name:
            profile_completion = profile_completion + 10
        if P.picture:
            profile_completion = profile_completion + 10
        if P.bio:
            profile_completion = profile_completion + 5
        if P.details_info:
            profile_completion = profile_completion + 5
        if C.mobile:
            profile_completion = profile_completion + 10
        if C.email:
            profile_completion = profile_completion + 10
        if C.address:
            profile_completion = profile_completion + 5
        if C.website:
            profile_completion = profile_completion + 5
        if C.facebook:
            profile_completion = profile_completion + 5
        if C.instagram:
            profile_completion = profile_completion + 5
        if C.twitter:
            profile_completion = profile_completion + 4    
        if C.telegram:
            profile_completion = profile_completion + 3
        if C.behance:
            profile_completion = profile_completion + 3

        return {
            'success': True,
            'fullname': U.first_name,
            'displayname': U.last_name,
            'account_mobile': U.mobile,
            'account_email': U.email,
            'portfolio_id': P.id,
            'profilepic': P.picture,
            'bio': P.bio,
            'details': P.details_info,
            'joining_date': P.joining_date,
            'rating': P.average_rating,
            'contact_mobile': C.mobile,
            'contact_email': C.email,
            'address': C.address,
            'facebook': C.facebook,
            'instagram': C.instagram,
            'twitter': C.twitter,
            'telegram': C.telegram,
            'whatsapp': C.whatsapp,
            'behance': C.behance,
            'website': C.website,
            'profile_completion': profile_completion
        }
    except:
        return {
            'success': False
        }
    

def UpdateProfileData(slug, displayname, mobile, email, address, bio, details, website, facebook, instagram, twitter, whatsapp, telegram, behance) -> bool:
    try:
        U = User.objects.get(slug=slug)
        P = Portfolio.objects.get(user_id=U.id)
        C = ContactInfo.objects.get(portfolio_id=P.id)

        U.last_name = displayname
        U.save()

        P.bio = bio
        P.details_info = details
        P.save()

        C.mobile = mobile
        C.email = email
        C.address = address
        C.website = website
        C.facebook = facebook
        C.instagram = instagram
        C.twitter = twitter
        C.whatsapp = whatsapp
        C.telegram = telegram
        C.behance = behance
        C.save()

        return True
    except:
        return False
    

def AddRecentWork(slug, title, description, files, date):
    try:
        server_url = None
        for filename, file in files.items():
            myfile = files[filename]
            folder_name = 'wp-seller/portfolio'
            myfile.name = change_file_name(myfile.name)
            server_url = file_upload_server(myfile, folder_name, f'/{folder_name}/')

        U = User.objects.get(slug=slug)
        P = Portfolio.objects.get(user_id=U.id)
        R = RecentWork(portfolio_id=P.id, title=title, description=description, picture=server_url, date=date)
        R.save()
        return True
    except:
        return False
    

def GetRecentWorks(portfolio_id):
    recent_works = RecentWork.objects.filter(portfolio_id=portfolio_id)
    list = []
    for r in recent_works:
        list.append({
           'title': r.title,
           'description': r.description,
           'thumbnail': r.picture,
           'date': r.date 
        })
    return list