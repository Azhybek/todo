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

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)

def add_book(request):
    form = request.POST
    bookstor = book(title=form['book-title'], subtitle=form['book-subtitle'],
                         description=form['book-description'], price=form['book-price'], genre=form['book-genre'], author=form['book-author'], year=form['book-year'])
    bookstor.save()

    return redirect(test2)

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)

def unmark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = False
    todo.save()
    return redirect(test)

# Create your views here.
