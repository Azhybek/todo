from django.shortcuts import render, HttpResponse

def homepage(request):
    return HttpResponse("Hello Azhy")

# Create your views here.
