from django.shortcuts import render
from blog.models import Posts, Comments
from .forms import CommentForm
# Create your views here.


def blog_index(request):
    all_posts = Posts.objects.all().order_by('-created')
    context = {'posts': all_posts}
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


    #comments = Comments.objects.get(post=post)
    context = {
        'post': post,
        #'comments': comments,
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