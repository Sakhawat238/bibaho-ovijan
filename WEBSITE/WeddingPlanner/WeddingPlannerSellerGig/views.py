from django.shortcuts import render, redirect
from django.contrib import messages
from WEBSITE.utils import seller_required, seller_self_required
from CORE.WeddingPlanner.WpService.services import get_service_list_min
from CORE.WeddingPlanner.WpGig.services import CreateGig, GetServiceWiseGigs, GetGigById
from CORE.WeddingPlanner.WpBookmark.services import GetBookmarkedGigIds


@seller_required()
def GigAdd(request):
    if request.method == "POST":
        r = request.POST
        slug = request.user.slug
        title = r.get('title')
        serviceid = r.get('service')
        location = r.get('location')
        description = r.get('details')
        basic_desc = r.get('basic_desc')
        basic_price = r.get('basic_price')
        basic_price_show = r.get('basic_price_show')
        standard_desc = r.get('standard_desc')
        standard_price = r.get('standard_price')
        standard_price_show = r.get('standard_price_show')
        premium_desc = r.get('premium_desc')
        premium_price = r.get('premium_price')
        premium_price_show = r.get('premium_price_show')
        custom_desc = r.get('custom_desc')
        custom_price = r.get('custom_price')
        custom_price_show = r.get('custom_price_show')

        faq_ids = r.get('total_faq').split(",")
        faq_list = []
        for faq in faq_ids:
            faq_list.append({
                'Q': r.get('question'+str(faq)),
                'A': r.get('answer'+str(faq))
            })

        success = CreateGig(slug,title,serviceid,location,description,basic_desc,basic_price,basic_price_show,
                  standard_desc,standard_price,standard_price_show,premium_desc,premium_price,premium_price_show,
                  custom_desc,custom_price,custom_price_show,request.FILES,faq_list)
        if success:
            messages.success(request, f'Service has been added successfully')
        else:
            messages.error(request, f'Something went wrong. Please try again.')

        return redirect("SellerProfile", slug)
        
    else:
        context = {
            'services': get_service_list_min()
        }
        return render(request, 'WEBSITE/WeddingPlanner/GigAdd.html', context)
    

def GigList(request):
    r = request.GET
    service_name = r.get('s')
    sort_by = r.get('o')
    gigs = GetServiceWiseGigs(service_name, sort_by)
    total_gigs = len(gigs)
    bookmarks = GetBookmarkedGigIds(request.user)
    giglist = []
    for g in gigs:
        bookmarked = False
        if g["id"] in bookmarks:
            bookmarked =True
        giglist.append({
            'g': g,
            'b': bookmarked
        })
    context = {
        'services': get_service_list_min(),
        'gigs': giglist,
        'total': total_gigs,
        'selected_service': service_name,
        'selected_sorting': sort_by
    }
    return render(request, 'WEBSITE/WeddingPlanner/GigList.html', context)


def GigView(request, id):
    context = {
        'data': GetGigById(request.user,id)
    }
    return render(request, 'WEBSITE/WeddingPlanner/GigView.html', context)


@seller_self_required()
def GigEdit(request, id, slug):
    context = {

    }
    return render(request, 'WEBSITE/WeddingPlanner/GigEdit.html', context)