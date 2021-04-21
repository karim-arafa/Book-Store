from django.shortcuts import render, redirect
from .forms import StoreForm
from .models import Store


def index(request):
    books = Store.objects.all()
    return render(request, 'store/index.html',{
        "books": books
    })


def create(request):
    form = StoreForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'store/create.html', {
        'form': form
    })


def edit(request, id):
    book = Store.objects.get(pk=id)
    form = StoreForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'store/edit.html', {
        'form': form,
        'book': book
    })


def delete(request, id):
    book = Store.objects.get(pk=id)
    book.delete()
    return redirect('index')
