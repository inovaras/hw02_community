from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Post, Group



def index(request):
    posts = Post.objects.all()[:10]
    print(posts)
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).all()[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)