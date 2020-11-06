from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
  return render(request, 'homeApp/home.html')
    
def contact(request):
  return render(request, 'homeApp/contact.html')

def about(request):
  return render(request, 'homeApp/about.html')