from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'Dreamerlixu/index.html',context={'post_lixt':post_list})
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'Dreamerlixu/detail.html', context={'post': post})