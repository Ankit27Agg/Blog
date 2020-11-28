from django.shortcuts import render,HttpResponse, redirect
from django.contrib import messages
from .models import Post, Postcomment

# Create your views here.
def blogHome(request):
  allPosts = Post.objects.all()
  context = {'allPosts': allPosts}
  messages.warning(request, 'WELCOME to the blog.')
  return render(request, 'blogApp/blogHome.html', context)

def blogPost(request, slug):
  post = Post.objects.filter(slug=slug).first()
  comment = Postcomment.objects.filter(post=comment)
  context = {'post': post, 'comment':comment}
  messages.warning(request, 'WELCOME to the blogPost.')
  return render(request, 'blogApp/blogPost.html', context)

def comments(request):
  if request.method=="POST":
      comment = request.POST.get('comment')
      user = request.user
      postSno = request.POST.get('postSno')
      post = Posts.objects.get(sno=postSno)
      parent = 

  return redirect("home")
