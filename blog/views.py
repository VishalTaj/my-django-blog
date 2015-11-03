from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from .models import Post
from django.utils import timezone
from .forms import PostForm

# def post_list(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'blog/post_list.html',{'posts':posts})
#
# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post })

class PostListView(ListView):
    model = Post
    queryset = Post.objects.all()
    print queryset

class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.all()
    print queryset


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            url = reverse('posts:post_detail',args=(),
                    kwargs={'pk':post.pk})
            return redirect(url)
    else:
        form = PostForm()
    return render(request, 'post_add.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            url = reverse('posts:post_detail',args=(),
                    kwargs={'pk':post.pk})
            return redirect(url)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})
