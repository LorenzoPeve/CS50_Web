from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone

from .models import User, Post, Following
from .models import EST

def index(request):
    posts = Post.objects.all().order_by('-created_at')
    context = {'posts': posts}
    return render(request, "network/index.html", context)


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
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


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
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

def create_post(request):

    if request.method == "POST":

        kwargs = dict(
            user=User.objects.get(username=request.user.username),
            content=request.POST["content"],
            created_at=datetime.now(EST)
        )

        new_post = Post(**kwargs)
        new_post.save()

    return HttpResponseRedirect(reverse("index"))

def display_profile(request, username: str):

    profile = User.objects.get(username=username)
    posts = Post.objects.filter(user=profile).order_by('-created_at')

    context = {
        'profile': profile,
        'posts': posts,
        'n_followers': len(profile.followers.all()),
        'n_followings': len(profile.following.all())
    }

    # Is the logged in user following the profile user 
    if request.user.is_authenticated:
        logged_in_user=User.objects.get(username=request.user.username)
        is_following = Following.objects.filter(
            user=logged_in_user, follows=profile).exists()
        context['is_following'] = is_following
    
    return render(request, "network/profile.html", context)

@login_required
def update_following(request):

    if request.method == "POST":
        
        logged_in_user=User.objects.get(username=request.user.username)
        profile_user=User.objects.get(
            username=request.POST["profile_username"])
        
        if request.POST["follow_choice"] == 'unfollow':
            Following.objects.filter(
                user=logged_in_user, follows=profile_user).delete()
        elif request.POST["follow_choice"] == 'follow':
            f = Following(user=logged_in_user, follows=profile_user)
            f.save()

    return HttpResponseRedirect(
        reverse("display_profile", args=[profile_user.username]))

@login_required
def display_following(request):

    user = User.objects.get(username=request.user.username)
    following = user.following.all()

    if len(following) == 0:
        posts = []
    else:
        following = [f.follows for f in following]
        posts = Post.objects.filter(user__in=following).order_by('-created_at')


    context = {'posts': posts}
    return render(request, "network/index.html", context)