from django.shortcuts                     import render, get_object_or_404, redirect
from django.utils                         import timezone
from django.contrib.auth.decorators       import login_required
from django.contrib.auth.models           import User
from .models                              import Post
from .forms                               import PostForm

def post_list(request):
    posts = Post.objects.filter(status=True).order_by('title')
    return render(request, 'ogevents/post_list.html', {'posts': posts})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'ogevents/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            user = User.objects.get(id=request.user.id)
            post.author_name = user.username
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('ogevents.views.post_list')
    else:
        form = PostForm()
    return render(request, 'ogevents/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            user = User.objects.get(id=request.user.id)
            post.author_name = user.username
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('ogevents.views.post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'ogevents/post_edit.html', {'form': form})

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post             = form.save(commit=False)
            user             = User.objects.get(id=request.user.id)
            post.author_name = user.username
            post.author      = request.user
            post.status      = False
            post.save()
            return redirect('ogevents.views.post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'ogevents/post_edit.html', {'form': form})
