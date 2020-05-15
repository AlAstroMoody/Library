from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic import ListView, View

from .forms import BookForm
from .models import BookModel


class Homepage(View):
    def get(self, request):
        books = BookModel.objects.all()
        random_books = BookModel.objects.order_by('time_added').filter(rating='5')[:4]
        return render(request, 'app/index.html', context={'books': books,
                                                          'random_books': random_books, 'about_me': True})


class Catalog(ListView):
    queryset = BookModel.objects.all()
    template_name = 'app/catalog.html'


class Library(View):
    def get(self, request):
        search_query = request.GET.get('search', '')
        if search_query:
            books = BookModel.objects.filter(Q(title__iregex=search_query) |
                                             Q(addition__iregex=search_query))
        else:
            books = BookModel.objects.all()
        paginator = Paginator(books, 5)
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        is_paginated = page.has_other_pages()
        if page.has_previous():
            prev_url = '?page={}'.format(page.previous_page_number())
        else:
            prev_url = ''
        if page.has_next():
            next_url = '?page={}'.format(page.next_page_number())
        else:
            next_url = ''
        search = True
        context = {'page_objects': page,
                   'is_paginated': is_paginated,
                   'prev_url': prev_url,
                   'next_url': next_url,
                   'search': search
                   }
        return render(request, 'app/library.html', context=context)


class BookDetails(View):
    def get(self, request, slug):
        book = get_object_or_404(BookModel, slug__iexact=slug)
        return render(request, 'app/book_details.html',
                      context={'book': book, 'detail': True})


class BookCreate(View):
    def get(self, request):
        form = BookForm()
        return render(request, 'app/book_create_form.html',
                      context={'form': form})

    def post(self, request):
        bound_form = BookForm(request.POST)
        if bound_form.is_valid():
            new_book = bound_form.save()
            return render(request, 'app/book_details.html',
                          context={'book': new_book})
        return render(request, 'app/book_create_form.html',
                      context={'form': bound_form})


class BookUpdate(View):
    def get(self, request, slug):
        book = get_object_or_404(BookModel, slug__iexact=slug)
        bound_form = BookForm(instance=book)
        return render(request, 'app/book_update_form.html',
                      context={'form': bound_form, 'book': book})

    def post(self, request, slug):
        book = get_object_or_404(BookModel, slug__iexact=slug)
        bound_form = BookForm(request.POST, instance=book)
        if bound_form.is_valid():
            new_book = bound_form.save()
            return render(request, 'app/book_details.html',
                          context={'book': new_book})
        return render(request, 'app/book_update_form.html',
                      context={'form': bound_form, 'book': book})


class BookDelete(View):
    def get(self, request, slug):
        book = get_object_or_404(BookModel, slug__iexact=slug)
        return render(request, 'app/book_delete.html', context={'book': book})

    def post(self, request, slug):
        book = get_object_or_404(BookModel, slug__iexact=slug)
        book.delete()
        return HttpResponseRedirect('/library/')
