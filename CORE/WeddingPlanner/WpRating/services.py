from .models import SellerRating


def GetSellerRecentRatings(portfolio_id):
    return SellerRating.objects.filter(portfolio_id=portfolio_id).only('id','date','rating',
        'rated_by','details').order_by('-date')[:3]

def GetSellerTopRating(portfolio_id):
    ratings = SellerRating.objects.filter(portfolio_id=portfolio_id).only('id','date','rating',
        'rated_by','details').order_by('-rating','-date')[:1]
    if len(ratings) > 0:
        return ratings[0]
    else:
        return None