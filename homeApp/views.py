from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
  return HttpResponse('This is HOME page of our app.')
    
def contact(request):
  return HttpResponse('This is Contact page of our app.')

def about(request):
  return HttpResponse('This is About page of our app.')