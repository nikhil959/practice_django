from django.shortcuts import render
from .models import Post

# Create your views here.


def post_list(request):
    posts = Post.objects.filter()
    return render(request, 'home.html', {'posts': posts})

