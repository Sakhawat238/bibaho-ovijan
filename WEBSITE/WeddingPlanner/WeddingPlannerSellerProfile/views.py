from django.shortcuts import render, redirect
from django.contrib import messages
from CORE.WeddingPlanner.WpSeller.services import GetProfileData, UpdateProfileData, AddRecentWork as AddRecentWorkService, GetRecentWorks
from CORE.WeddingPlanner.WpRating.services import GetSellerRecentRatings
from CORE.WeddingPlanner.WpGig.services import GetSellerGigs
from WEBSITE.utils import seller_self_required, seller_required


def SellerProfile(request, slug):
    if not request.user.is_anonymous and request.user.slug == slug:
        return SellerProfileSelfView(request, slug)
    else:
        return SellerProfilePublicView(request, slug)



def SellerProfileSelfView(request, slug):
    profile_data = GetProfileData(slug)
    context = {
        'slug': slug,
        'data': profile_data,
        'ratings': GetSellerRecentRatings(profile_data["portfolio_id"]),
        'gigs': GetSellerGigs(profile_data["portfolio_id"]),
        'recent_works': GetRecentWorks(profile_data["portfolio_id"])
    }
    return render(request, 'WEBSITE/WeddingPlanner/SellerProfile.html', context)


def SellerProfilePublicView(request, slug):
    profile_data = GetProfileData(slug)
    context = {
        'slug': slug,
        'data': profile_data,
        'ratings': GetSellerRecentRatings(profile_data["portfolio_id"]),
        'gigs': GetSellerGigs(profile_data["portfolio_id"]),
        'recent_works': GetRecentWorks(profile_data["portfolio_id"])
    }
    return render(request, 'WEBSITE/WeddingPlanner/SellerProfilePublic.html', context)



@seller_self_required()
def SellerProfileEdit(request, slug, a="sss"):
    if request.method == "POST":
        r = request.POST
        name = r.get('display_name')
        mobile = r.get('mobile_no')
        email = r.get('email_address')
        address = r.get('address')
        bio = r.get('bio')
        details = r.get('details')
        website = r.get('web_site')
        facebook = r.get('face_book')
        instagram = r.get('insta_gram')
        twitter = r.get('twit_ter')
        whatsapp = r.get('whats_app')
        telegram = r.get('tele_gram')
        behance = r.get('be_hance')

        success = UpdateProfileData(slug, name, mobile, email, address, bio, details, website, facebook, instagram, twitter, whatsapp, telegram, behance)
        if success:
            messages.success(request, f'Proile information updated successfully')
            return redirect("SellerProfile", slug)
        else:
            messages.error(request, f'Profile information update failed.')
            return redirect("SellerProfileEdit", slug)
    else:
        context = {
            'data': GetProfileData(slug)
        }
        return render(request, 'WEBSITE/WeddingPlanner/SellerProfileEdit.html', context)
    

@seller_required()
def AddRecentWork(request):
    if request.method == 'POST':
        r = request.POST
        title = r.get('title')
        details = r.get('details')
        date = r.get('date')
        slug = request.user.slug
        success = AddRecentWorkService(slug, title, details, request.FILES, date)
        if success:
            messages.success(request, f'Recent works updated successfully')
            return redirect("SellerProfile", slug)
        else:
            messages.error(request, f'Recent works update failed.')
            return redirect("SellerProfile", slug)
    else:
        context = {}
        return render(request, 'WEBSITE/WeddingPlanner/RecentWorksAdd.html', context)
