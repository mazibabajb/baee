
from django.shortcuts import render
from .models import Book

# Create your views here.

def book_list(request):
    books = Book.objects.all()
    context = {
        'books':books
    }
    return render(request,"books/book_list.html",context)


def book_detail(request, id):
    return render(request,"books/book_list.html")

def book_detail(request, id):
    books = Book.objects.get(id=id)
    context = {
		'books': books,	
	}
    return render(request, "books/book_detail.html",context)    