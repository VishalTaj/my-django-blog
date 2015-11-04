from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.http import HttpResponse
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.contrib.auth.models import User
from django.db.models import Q
import json
from django.core import serializers

# def post_list(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'blog/post_list.html',{'posts':posts})
#
# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post })

class PostListView(ListView):
    model = Post
    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        user = self.request.user
        if user == 'vishal':
            return Post.objects.filter(author=user)
        else:
            return Post.objects.all()


    # queryset = get_object_or_404(Post, author=author)
    # print queryset

class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.all()


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

def post_title(request):
    if request.method == "POST":
        title = request.POST.get('title')
        if Post.objects.filter(title = title):
            print title
            return HttpResponse("error occured")
        else:
            return HttpResponse("No issues")

def search_box(request):
    if request.is_ajax():
        q = request.GET.get( 'q' )
        if q is not None:
            ser_results = serializers.serialize('json', Post.objects.filter(
                Q( title__contains = q )))
            print ser_results
            mimetype = 'application/json'
            return HttpResponse({'data': ser_results},content_type='application/json')
        else:
            return HttpResponse("im Not None")

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
