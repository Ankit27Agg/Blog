from django.shortcuts import render,HttpResponse
from django.contrib import messages

# Create your views here.
def blogHome(request):
  messages.warning(request, 'WELCOME to the blog.')
  return render(request, 'blogApp/blogHome.html')

def blogPost(request, slug):
  messages.warning(request, 'WELCOME to the blogPost.')
  return render(request, 'blogApp/blogPost.html')
