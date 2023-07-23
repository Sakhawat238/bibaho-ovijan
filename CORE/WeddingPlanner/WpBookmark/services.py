from .models import BookmarkGig, BookmarkSeller
from AUTH.UserAuthentication.models import USER_TYPE


def CreateGigBookmark(userid, gigid, remarks):
    try:
        BG = BookmarkGig(user_id=userid, gig_id=gigid, remarks=remarks)
        BG.save()
        return True
    except:
        return False
    

def CreateSellerBookmark(userid, portfolioid, remarks):
    try:
        BG = BookmarkSeller(user_id=userid, seller_id=portfolioid, remarks=remarks)
        BG.save()
        return True
    except:
        return False
    

def GetBookmarkedGigIds(user):
    if not user.is_anonymous:
        if user.type == USER_TYPE.VISITOR:
            return list(BookmarkGig.objects.filter(user_id=user.id).values_list('gig_id', flat=True))
    return []


def CheckBookMarkGigExists(userid, gigid):
    return BookmarkGig.objects.filter(user_id=userid, gig_id=gigid).exists()


def GetBookmarkedGigs(user):
    return BookmarkGig.objects.select_related('gig').filter(user_id=user.id
        ).only('id','gig__id','gig__title','remarks', 'created_at')


def CheckBookMarkSellerExists(userid, portfolioid):
    return BookmarkSeller.objects.filter(user_id=userid, seller_id=portfolioid).exists()


def GetBookmarkedSellers(user):
    return BookmarkSeller.objects.select_related('seller').filter(user_id=user.id)