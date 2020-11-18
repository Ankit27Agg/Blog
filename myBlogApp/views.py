from django.shortcuts import render,HttpResponse
from django.contrib import messages
from .models import Post

# Create your views here.
def blogHome(request):
  allPosts = Post.objects.all()
  context = {'allPosts': allPosts}
  messages.warning(request, 'WELCOME to the blog.')
  return render(request, 'blogApp/blogHome.html', context)

def blogPost(request, slug):
  post = Post.objects.filter(slug=slug).first()
  context = {'post': post}
  messages.warning(request, 'WELCOME to the blogPost.')
  return render(request, 'blogApp/blogPost.html', context)

