from django.shortcuts import render
from django.http import JsonResponse
from WEBSITE.utils import visitor_required
from CORE.WeddingPlanner.WpBookmark.services import CreateSellerBookmark, CreateGigBookmark, GetBookmarkedGigs, GetBookmarkedSellers


@visitor_required()
def AddBookmark(request):
    r = request.GET
    userid = request.user.id
    b_type = r.get('type')
    b_id = r.get('id')
    remarks = r.get('remarks')

    if b_type == 'service':
        success = CreateGigBookmark(userid, b_id, remarks)
    elif b_type == 'seller':
        success = CreateSellerBookmark(userid, b_id, remarks)

    return JsonResponse ({
        "success": success
    })


@visitor_required()
def BookmarkList(request):
    gigs = GetBookmarkedGigs(request.user)
    sellers = GetBookmarkedSellers(request.user)
    context = {
        'gigs': gigs,
        'sellers': sellers
    }
    return render(request, 'WEBSITE/WeddingPlanner/Bookmarks.html', context)