from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("random/", views.random_page, name="random_entry"),
    path("query/", views.query, name="query"),
    path("<str:entry>", views.display_entry, name="entry"),
]
