from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Posts
# Create your views here.


def blog_index(request):
    all_posts = Posts.objects.all()
    return render(request, 'blog/blog_index.html', {"posts": all_posts})
