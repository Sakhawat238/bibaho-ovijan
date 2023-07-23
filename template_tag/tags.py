from django import template
from AUTH.UserAuthentication.models import USER_TYPE
from CORE.WeddingPlanner.WpSeller.models import Portfolio
import math


register = template.Library()

@register.inclusion_tag('TemplateTags/NavbarRight.html')
def profile_load(requests):
    userObj = requests.user
    loggedin = not userObj.is_anonymous
    profilepic = None
    if loggedin:
        if userObj.type == USER_TYPE.ADMIN:
            pass
        elif userObj.type == USER_TYPE.VISITOR:
            pass
        elif userObj.type == USER_TYPE.SELLER:
            P = Portfolio.objects.get(user_id=userObj.id)
            profilepic = P.picture
    return {
        'loggedin': loggedin,
        'type': userObj.type if loggedin else "",
        'pic': profilepic,
        'slug': userObj.slug if loggedin else ""
    }


@register.inclusion_tag('TemplateTags/RatingShow.html')
def show_rating(rating):
    full_star = math.floor(rating)
    empty_star = 5 - math.ceil(rating)
    half_star = 5 - (full_star + empty_star)
    return {
        'fs': range(full_star),
        'hs': range(half_star),
        'es': range(empty_star)
    }


@register.simple_tag()
def show_bookmark(request):
    if not request.user.is_anonymous and request.user.type == USER_TYPE.VISITOR:
        return 'inline-block'
    else:
        return 'none'


# @register.filter
# def reference_id(user_id, prefix):
#     return prefix + str(user_id).zfill(8)