from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createlisting", views.create_listing, name="createlisting"),
    path("shopcategory/<str:category>/", views.shop_by_category, name="shopcategory"),
    path("shopcategory", views.shop_by_category, name="shopcategory"),
    path("watchlist", views.add_to_watchlist, name="watchlist"),
    path("removefromwatchlist", views.remove_from_watchlist, name="removefromwatchlist"),
    path("mywatchlist", views.display_watchlist, name="mywatchlist"),
    path("listing/<int:listing_id>", views.display_listing, name="showlisting"),
    path("add_comment/", views.add_comment, name="addcomment"),
    path("place_bid/", views.place_bid, name="placebid"),
]
