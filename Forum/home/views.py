from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.shortcuts import render
from django.http import HttpResponse
import mimetypes
from django.db.models import Q
from .models import Post, Comment
from .forms import PostForm, CommentForm

ROLE_CHOICES = (
    ('Year', 'YEAR'),
    ('Department', 'DEPARTMENT'),
    ('All', 'ALL')
)

def index(request):
	posts = Post.objects.all()
	# Login Required
	if request.user.is_authenticated:
		return render(request, 'home/index.html', {'posts': posts, 'users': User.objects.all()})
	else:
		return render(request, 'accounts/login.html')


def details(request, post_id):
    post = Post.objects.get(pk=post_id)
    comments = Comment.objects.filter(post=post)
    return render(request, 'home/details.html', {'post': post, 'comments': comments})


def create_post(request):
    form = PostForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        title = form.cleaned_data['title']

        for a in Post.objects.all():
            if title == a.title:
                context = {
                    'post': post,
                    'form': form,
                    'error_message': "Title already exists",
                }
                return render(request, 'home/post_form.html', context)
        post.save()
        return render(request, 'home/details.html', {'post': post})
    return render(request, 'home/post_form.html', {'form': form})


def edit_post(request, post_id):
    post = Post.objects.get(pk=post_id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'home/details.html', {'post': post})
    else:
        form = PostForm(instance=post)
        return render(request, 'home/post_form.html', {'form': form})


def delete_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    posts = Post.objects.all()
    return render(request, 'home/index.html', {'posts': posts})


def add_comment(request, post_id):
    post = Post.objects.get(pk=post_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            comments = Comment.objects.filter(post=post)
            return render(request, 'home/details.html', {'post': post, 'comments': comments})
    else:
        form = CommentForm()
    return render(request, 'home/comment_form.html', {'form': form})


def delete_comment(request, post_id, comment_id):
    post = Post.objects.get(pk=post_id)
    comment = Comment.objects.get(pk=comment_id)
    comment.delete()
    context = {
        'post': post,
        'comments': Comment.objects.filter(post=post),
    }
    return render(request, 'home/details.html', context)


def search(request):
    query = request.GET.get("q")
    users = User.objects.all()
    users = users.filter(
            Q(username__icontains=query)
        ).distinct()
    posts = Post.objects.all()
    posts = posts.filter(
            Q(title__icontains=query)
        ).distinct()
    context = {
        'posts': posts,
        'users': users,
    }
    return render(request, 'home/search.html', context)
