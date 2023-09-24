from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.paginator import Paginator

from .models import User, Post, Following, Like
from .models import EST

def index(request):
    
    posts = Post.objects.all().order_by('-created_at')
    p = Paginator(posts, 10)
    page = request.GET.get('page')
    paginated_posts = p.get_page(page)
    context = {'paginated_posts': paginated_posts}
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

        current_ts = datetime.now(EST)
        kwargs = dict(
            user=User.objects.get(username=request.user.username),
            content=request.POST["content"],
            created_at=current_ts,
            updated_at=current_ts,
        )

        new_post = Post(**kwargs)
        new_post.save()

    return HttpResponseRedirect(reverse("index"))

def display_profile(request, username: str):

    profile = User.objects.get(username=username)
    posts = Post.objects.filter(user=profile).order_by('-created_at')
    p = Paginator(posts, 10)
    page = request.GET.get('page')
    paginated_posts = p.get_page(page)
    context = {
        'profile': profile,
        'paginated_posts': paginated_posts,
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

    p = Paginator(posts, 10)
    page = request.GET.get('page')
    paginated_posts = p.get_page(page)
    context = {'paginated_posts': paginated_posts}
    return render(request, "network/index.html", context)

@csrf_exempt
@login_required
def like_unlike_post(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    
    data = json.loads(request.body)
    post_id = data['post_id']
    post = Post.objects.get(id=post_id)

    l = Like.objects.filter(user=request.user, post=post)

    if l.exists():
        l[0].delete()
        return JsonResponse('dislike', safe=False)
    else:     
        l = Like(user=request.user, post=post)
        l.save()
        return JsonResponse('like', safe=False)

@csrf_exempt
@login_required
def update_post(request):
    
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    
    data = json.loads(request.body)
    post_id = data['post_id']
    new_content = data['content']

    # Update post
    try:
        post = Post.objects.get(id=post_id)
        post.content = new_content
        post.updated_at = datetime.now(EST)
        post.save()
        return JsonResponse('Post was updated', safe=False)
    except Exception:
        return JsonResponse("Post couldn't be updated", status=400)


