
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("post", views.create_post, name="createpost"),
    path("profile/<str:username>", views.display_profile, name="display_profile"),
    path('followers', views.update_following, name="followers"),
    path('following', views.display_following, name="post-following"),

]
