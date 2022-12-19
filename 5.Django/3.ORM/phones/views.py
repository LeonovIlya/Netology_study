from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_by = request.GET.get('sort')
    print(sort_by)
    template = 'catalog.html'
    phones = Phone.objects.all()

    if sort_by == 'name':
        result = phones.order_by('name')
    elif sort_by == 'min_price':
        result = phones.order_by('price')
    elif sort_by == 'max_price':
        result = phones.order_by('-price')
    else:
        result = phones

    context = {'phones': result}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
