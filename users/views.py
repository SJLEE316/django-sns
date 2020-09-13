from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import User
from posts.models import Post

@login_required
def follow_toggle(request, id):
    user = request.user
    profile=user.profile

    followed_user = get_object_or_404(User, pk=id)

    is_follower=user.profile in followed_user.profile.followers.all()

    if is_follower:
        profile.followings.remove(followed_user.profile)
    else:
        profile.followings.add(followed_user.profile)

    return redirect('home')   

def mypage(request, id):
    mypage_user = get_object_or_404(User, pk=id)
    context = {
        'posts' : Post.objects.filter(user=mypage_user),
        'followings' : mypage_user.profile.followings.all(),
        'followers' : mypage_user.profile.followers.all(),
    }
    return render(request, 'users/mypage.html', context)

# Create your views here.
