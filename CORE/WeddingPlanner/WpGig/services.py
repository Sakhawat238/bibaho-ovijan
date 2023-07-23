from django.db.models import F
from .models import Gig, Gallary, Package, PackageType, SellerFaq
from AUTH.UserAuthentication.models import User, USER_TYPE
from CORE.WeddingPlanner.WpSeller.models import Portfolio
from CORE.WeddingPlanner.WpService.models import Service
from CORE.WeddingPlanner.WpService.services import update_service_seller_count
from CORE.WeddingPlanner.WpRating.services import GetSellerTopRating
from CORE.WeddingPlanner.WpBookmark.services import CheckBookMarkGigExists
from CORE.utils import change_file_name, file_upload_server



def CreateGig(slug,title,service_id,location,description,basic_desc,basic_price,basic_price_show,
              standard_desc,standard_price,standard_price_show,premium_desc,premium_price,premium_price_show,
              custom_desc,custom_price,custom_price_show,files,faqs):
    try:
        U = User.objects.get(slug=slug)
        P = Portfolio.objects.get(user_id=U.id)
        G = Gig(title=title,portfolio_id=P.id,service_type_id=service_id,location=location,description=description,thumbnail=None)
        G.save()
    except:
        return False

    try:
        package_list = []
        if basic_desc:
            price = basic_price if basic_price else "Not specified"
            bps = True if basic_price_show else False
            package_list.append(Package(gig_id=G.id,category=PackageType.BASIC,description=basic_desc,price=price,show_price=bps))
        if standard_desc:
            price = standard_price if standard_price else "Not specified"
            sps = True if standard_price_show else False
            package_list.append(Package(gig_id=G.id,category=PackageType.STANDARD,description=standard_desc,price=price,show_price=sps))
        if premium_desc:
            price = premium_price if premium_price else "Not specified"
            pps = True if premium_price_show else False
            package_list.append(Package(gig_id=G.id,category=PackageType.PREMIUM,description=premium_desc,price=price,show_price=pps))
        if custom_desc:
            price = custom_price if custom_price else "Not specified"
            cps = True if custom_price_show else False
            package_list.append(Package(gig_id=G.id,category=PackageType.CUSTOM,description=custom_desc,price=price,show_price=cps))
        Package.objects.bulk_create(package_list)

        faqs_list = []
        for f in faqs:
            faqs_list.append(SellerFaq(gig_id=G.id, question=f['Q'], answer=f['A']))
        SellerFaq.objects.bulk_create(faqs_list)

        for filename, file in files.items():
            myfile = files[filename]
            if filename == 'thumbnail':
                folder_name = 'wp-seller/service'
                myfile.name = change_file_name(myfile.name)
                server_url = file_upload_server(myfile, folder_name, f'/{folder_name}/')
                G.thumbnail = server_url
                G.save()
            else:
                folder_name = 'wp-seller/service'
                myfile.name = change_file_name(myfile.name)
                server_url = file_upload_server(myfile, folder_name, f'/{folder_name}/')
                GL = Gallary(gig_id=G.id, file=server_url)
                GL.save()

        update_service_seller_count(service_id,1)

    except:
        G.delete()
        return False
    
    return True


def GetSellerGigs(portfolio_id):
    gigs = Gig.objects.filter(portfolio_id=portfolio_id).only('id','thumbnail','title').order_by('-id')
    gig_list = []
    for g in gigs:
        gig_list.append({
            'id': g.id,
            'title': g.title,
            'thumbnail': g.thumbnail
        })
    return gig_list


def GetServiceWiseGigs(service_name, order_by):
    if service_name is not None and service_name !="":
        try:
            S = Service.objects.get(title=service_name)
            gigs = Gig.objects.select_related('portfolio', 'portfolio__user').filter(service_type_id=S.id).only(
                'id','portfolio__id','portfolio__user__id','title','thumbnail','portfolio__user__last_name',
                'portfolio__picture','portfolio__average_rating')
        except:
            gigs = Gig.objects.select_related('portfolio', 'portfolio__user').only(
                'id','portfolio__id','portfolio__user__id','title','thumbnail','portfolio__user__last_name',
                'portfolio__picture','portfolio__average_rating')
    else:
        gigs = Gig.objects.select_related('portfolio', 'portfolio__user').only(
                'id','portfolio__id','portfolio__user__id','title','thumbnail','portfolio__user__last_name',
                'portfolio__picture','portfolio__average_rating')
    
    if order_by is not None and order_by !="":
        if order_by == 'R':
            gigs = gigs.order_by('-portfolio__average_rating')
        elif order_by == 'T':
            gigs = gigs.order_by('-created_at')
    else:
        gigs = gigs.order_by('-created_at')
    
    gig_list = []
    for g in gigs:
        gig_list.append({
            'id': g.id,
            'title': g.title,
            'thumbnail': g.thumbnail,
            'seller': g.portfolio.user.last_name,
            'rating': g.portfolio.average_rating,
            'propic': g.portfolio.picture
        })
    return gig_list


def GetGigById(requested_user, id):
    gig = Gig.objects.select_related('portfolio','portfolio__user').get(id=id)
    portfolio = gig.portfolio
    user = portfolio.user
    toprating = GetSellerTopRating(portfolio.id)
    tags = portfolio.sellertag_set.select_related('tag').all()
    gallarys = Gallary.objects.filter(gig_id=gig.id)
    packages = Package.objects.filter(gig_id=gig.id)
    basic = None
    standard = None
    premium = None
    custom = None
    for p in packages:
        if p.category == PackageType.BASIC:
            basic = p
        elif p.category == PackageType.STANDARD:
            standard = p
        elif p.category == PackageType.PREMIUM:
            premium = p
        elif p.category == PackageType.CUSTOM:
            custom = p
    faqs = SellerFaq.objects.filter(gig_id=gig.id)
    bookmarked = False
    if not requested_user.is_anonymous:
        if requested_user.type == USER_TYPE.VISITOR:
            bookmarked = CheckBookMarkGigExists(requested_user.id, gig.id)
    return {
        'gig': gig,
        'portfolio': portfolio,
        'user': user,
        'toprating': toprating,
        'gallarys': gallarys,
        'basic': basic,
        'standard': standard,
        'premium': premium,
        'custom': custom,
        'faqs': faqs,
        'tags': tags,
        'bookmarked': bookmarked
    }


    