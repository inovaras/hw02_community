from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Post, Group
from .consts import POSTS_NUMBERS


def index(request):
    posts = Post.objects.all()[:POSTS_NUMBERS]
    print(posts)
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).all()[:POSTS_NUMBERS]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
