from django.shortcuts import render,HttpResponse

# Create your views here.
def blogHome(request):
  return HttpResponse('This is HOME page of our blog app.')

def blogPost(request, slug):
  return HttpResponse(f'This is blogPost: {slug}')
