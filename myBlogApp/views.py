from django.shortcuts import render,HttpResponse

# Create your views here.
def home(index):
  return HttpResponse('This is HOME page of our app.')