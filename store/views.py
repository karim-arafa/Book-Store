from django.shortcuts import render, redirect
from .forms import StoreForm, CatForm
from .models import Store
from django.contrib.auth.decorators import login_required, permission_required


@login_required(login_url="/login")
@permission_required(["store.view_store"], raise_exception=True)
def index(request):
    books = Store.objects.all()
    return render(request, 'store/index.html', {
        "books": books
    })

@login_required
def create(request):
    form = StoreForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'store/create.html', {
        'form': form
    })

@login_required
def createCat(request):
    form = CatForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'store/createCat.html', {
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
