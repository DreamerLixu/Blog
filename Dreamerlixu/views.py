from .models import Post
from django.shortcuts import render, get_object_or_404
import markdown


def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'Dreamerlixu/index.html',context={'post_list':post_list})
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request, 'Dreamerlixu/detail.html', context={'post': post})