from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from . models import Post
from .forms import PostForm
# Create your views here.

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})


def post_detail(request, pk):
	posts = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post':posts})

def post_new(request):
	form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})