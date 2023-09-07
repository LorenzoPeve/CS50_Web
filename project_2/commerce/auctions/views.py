from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import User, Listing, Watchlist, Comment
from .models import CATEGORIES


def index(request):

    if request.user.is_authenticated:
        listings = Listing.objects.all()
        return render(
            request, "auctions/index.html", {'listings': listings})
    else:
        return render(request, "auctions/login.html", {
                "message": "Must sign in to see listings"
            })
    
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
    
@login_required()
def create_listing(request):

    if request.method == "POST":

        kwargs = dict(
            owner=User.objects.get(username=request.user.username),
            title=request.POST["title"],
            description=request.POST["content"],
            current_bid=request.POST.get("starting_bid"),
            category=request.POST["category"],
        )
        url = request.POST.get("image_url")
        if len(url) > 0:
            kwargs['image_url'] = url

        new_listing = Listing(**kwargs)
        new_listing.save()
        return redirect('index')
    else:
        return render(request, "auctions/create.html", {
            'categories': CATEGORIES})
    
@login_required()
def shop_by_category(request, category: str=None):

    if category is None:
        return render(request, "auctions/category.html", {
            'categories': CATEGORIES})

    elif category == 'all' or len(category) == 0:
        listings = Listing.objects.all()
        return render(
            request, "auctions/index.html", {'listings': listings})

    else:
        listings = Listing.objects.filter(category=category)
        return render(
            request, "auctions/index.html", {
                'listings': listings, 'category': category})
      
@login_required()
def add_to_watchlist(request):

    user = User.objects.get(username=request.user.username)
    listing = Listing.objects.get(id=request.POST["listing_id"])
    
    w = Watchlist(user=user, listing=listing)
    try:
        w.save()
    except IntegrityError as e:
        assert e.args[0].startswith('UNIQUE constraint failed')

    return display_watchlist(request)

@login_required()
def remove_from_watchlist(request):

    user = User.objects.get(username=request.user.username)
    listing = Listing.objects.get(id=request.POST["listing_id"])    
    w = Watchlist.objects.filter(user=user, listing=listing)
    w.delete()
    return display_watchlist(request)


@login_required()
def display_watchlist(request):

    specific_user = User.objects.get(username=request.user.username)
    watchlist_items = Watchlist.objects.filter(user=specific_user)
    listings = [item.listing for item in watchlist_items]
    return render(request, "auctions/mywatchlist.html", {'listings': listings})


def _is_listing_in_users_watchlist(listing_id: int, user: User) -> bool:
    """Returns True is listing is already in User's watchlist"""

    ls = Listing.objects.get(id=listing_id)
    w = Watchlist.objects.filter(user=user, listing=ls)
    if len(w) == 0:
        return False
    return True

def _does_user_owns_listing(l: Listing, user: User) -> bool:
    """Returns True is listing is already in User's watchlist"""

    if l.owner.username == user.username:
        return True
    return False

@login_required()
def display_listing(request, listing_id: int):

    specific_user = User.objects.get(username=request.user.username)
    listing = Listing.objects.get(id=listing_id)

    is_in_watchlist = _is_listing_in_users_watchlist(listing_id, specific_user)
    is_user_owner = _does_user_owns_listing(listing, specific_user)
    comments = Comment.objects.filter(listing=listing).order_by('date')

    return render(request, "auctions/listing.html", {
            'listing': listing,
            'is_in_users_watchlist': is_in_watchlist,
            'is_user_owner': is_user_owner,
            'comments': comments
    }
    )

@login_required()
def add_comment(request):

    specific_user = User.objects.get(username=request.user.username)
    listing = Listing.objects.get(id=request.POST["listing_id"])
    c = Comment(
        listing=listing,
        author=specific_user,
        date=datetime.now(),
        comment=request.POST["comment"]
    )
    c.save()
    
    return display_listing(request, request.POST["listing_id"])

@login_required()
def place_bid(request):

    specific_user = User.objects.get(username=request.user.username)
    listing = Listing.objects.get(id=request.POST["listing_id"])
    c = Comment(
        listing=listing,
        author=specific_user,
        date=datetime.now(),
        comment=request.POST["comment"]
    )
    c.save()
    
    return display_listing(request, request.POST["listing_id"])