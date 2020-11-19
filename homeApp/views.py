from django.shortcuts import render, HttpResponse
from .models import Contact
from django.contrib import messages
from myBlogApp.models import Post

# Create your views here.

def home(request):
  messages.info(request, 'WELCOME to the home page.')
  return render(request, 'homeApp/home.html')
    
def contact(request):
  messages.warning(request, 'WELCOME to the contact us page.')
  if request.method=="POST":
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    desc = request.POST['desc']
    if len(name)<4 or len(email)<10 or len(phone)<10 or len(desc)<1:
      messages.error(request, 'PLEASE fill the form correctly.')
    else:
      contact = Contact(name=name, email=email, phone=phone, description=desc)
      contact.save()
      messages.success(request, 'FORM recorded successfully')

  return render(request, 'homeApp/contact.html')

def about(request):
  messages.warning(request, 'WELCOME to the about us page.')
  return render(request, 'homeApp/about.html')


def search(request):
  messages.success(request, 'WELCOME to the about us page.')
  query = request.GET['result'];
  if len(query) >= 50:
    allPosts = Posts.objects.none()
  else:
    allPostsTitle = Post.objects.filter(title__icontains=query)
    allPostsContent = Post.objects.filter(content__icontains=query)
    allPostsAuthor = Post.objects.filter(author__icontains=query)
    allPosts = allPostsTitle.union(allPostsContent, allPostsAuthor)
    context = {'allPosts': allPosts, "result": query}

  return render(request, 'homeApp/search.html', context)