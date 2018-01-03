from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,Category
from django.shortcuts import render, get_object_or_404
import markdown

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    title = Category.objects.get(id=2)

    return render(request, 'blog/index.html', context={
        'post_list': post_list,
        'title' : title
    })

def detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    title = Post.objects.get(id=3)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    return render(request, 'blog/detail.html', context={
        'post': post,
        'title': title
    })
# Create your views here.
