from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo
from .models import ToDo, book

def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def test2(request):
    book_list = book.objects.all()
    return render(request, "book.html", {"book_list": book_list})

# Create your views here.
