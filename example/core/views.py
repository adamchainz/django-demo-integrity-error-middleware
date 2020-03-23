from django.http import HttpResponse

from example.core.models import Book


def index(request):
    book = Book.objects.create(title="War and Peace")
    return HttpResponse(f"It's {book.title}")
