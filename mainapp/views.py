from django.shortcuts import render

from mainapp.models import Product, ProductCategory
from django.views.generic.list import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'mainapp/index.html', context)

class ProductsListView(ListView):
    model = Product
    template_name = 'mainapp/products.html'

    def get_context_data(self, **kwargs):
        context = super(ProductsListView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Каталог'
        context['categories'] = ProductCategory.objects.all()
        context['products'] = Product.objects.all()
        return context
    def get(self, request, *args, **kwargs):
        pass
#def products(request, category_id=None, page=1):
#    context = {'title': 'GeekShop - Каталог', 'categories': ProductCategory.objects.all()}
#    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
#    paginator = Paginator(products, per_page=2)
#    try:
#        products_paginator = paginator.page(page)
#    except PageNotAnInteger:
#        products_paginator = paginator.page(1)
#    except EmptyPage:
#        products_paginator = paginator.page(paginator.num_pages)
#    context.update({'products': products_paginator})
#    return render(request, 'mainapp/products.html', context)
