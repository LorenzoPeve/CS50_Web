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
]
