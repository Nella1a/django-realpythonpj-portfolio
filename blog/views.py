from django.shortcuts import render
from blog.models import Posts, Comments
from .forms import CommentForm, PostsForm
# Create your views here.
import datetime

def blog_index(request):

    form = PostsForm()
    if request.method == 'POST':
        form = PostsForm(request.POST)
        if form.is_valid():
            new_post = Posts(
                title=form.cleaned_data["title"],
                text=form.cleaned_data["text"],
                created=datetime.datetime.now(),
                last_update=datetime.datetime.now(),
            )

            new_post.save()
            new_post.category.set(form.cleaned_data["category"])
            new_post.save()

    all_posts = Posts.objects.all().order_by('-created')

    context = {'posts': all_posts,
               'form': form}

    return render(request, 'blog/blog_index.html', context)

def blog_detail(request, pk):
    post = Posts.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comments(
                author=form.cleaned_data["author"],
                text=form.cleaned_data["text"],
                post=post
            )
            comment.save()


    comments = Comments.objects.filter(post=post.pk)
    context = {
        'post': post,
        'comments': comments,
        "form": form,
    }
    return render(request, 'blog/blog_detail.html', context)

def blog_category(request, category):
    posts = Posts.objects.filter(category__name__contains=category).order_by(
        '-created'
    )

    context = {
        'category': category,
        'posts': posts
    }
    return render(request, "blog/blog_category.html", context)