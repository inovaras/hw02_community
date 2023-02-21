from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Post, Group
from django.conf import settings
from django.contrib.auth.decorators import login_required


@login_required()
def index(request):
    posts = Post.objects.all()[: settings.POSTS_NUMBERS]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).all()[: settings.POSTS_NUMBERS]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
