from django.urls import path, include

urlpatterns = [
    path('home/', include('WEBSITE.WeddingPlanner.WeddingPlannerLandingpage.urls')),
    path('seller-profile/', include('WEBSITE.WeddingPlanner.WeddingPlannerSellerProfile.urls')),
    path('seller-services/', include('WEBSITE.WeddingPlanner.WeddingPlannerSellerGig.urls')),
    path('bookmark/', include('WEBSITE.WeddingPlanner.WeddingPlannerBuyerBookmark.urls')),
    path('wedding-plan/', include('WEBSITE.WeddingPlanner.WeddingPlannerPlan.urls'))
]