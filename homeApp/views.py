from django.shortcuts import render, HttpResponse, redirect
from .models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from myBlogApp.models import Post

# Create your views here.

def home(request):
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




def signupManager(request):
  if request.method == 'POST':
    
    uname = request.POST['uname']
    ename = request.POST['ename']
    passwordName = request.POST['pname']
    firstName = request.POST['fname']
    lastName = request.POST['lname']
    passwordName = request.POST['pname']
    confirmpasswordName = request.POST['cpname']

    if len(passwordName)  > 10:
      messages.error(request, 'password should be of less than 11 characters')
      return redirect('home')

    if passwordName != confirmpasswordName:
      messages.error(request, 'confirm password is not same as password')
      return redirect('home')

    newUser = User.objects.create_user(uname, ename, passwordName)
    newUser.first_name = firstName
    newUser.last_name = lastName
    newUser.save()
    messages.success(request, 'WELCOME to our company. Yo\'re info has been saved successfully. ')
    return redirect('home')
  
  else:
    return HttpResponse("TRY AGAIN")


# login manager
def loginManager(request):
  usernamename = request.POST['usernamename']
  passwordname = request.POST['passwordname']
  return HttpResponse(' You\'re login. ENJOY blogs.')


# logout manager
def logoutManager(request):
  return HttpResponse('logout')
