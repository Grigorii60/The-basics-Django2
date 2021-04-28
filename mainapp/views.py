from django.shortcuts import render

# Create your views here.

def index(request):
    contex = {
        'title': 'geekShop',
    }
    return  render(request, 'mainapp/index.html', contex)

def products(request):
    contex = {
        'title': 'GeekShop-каталог',
        'product': 'Отличный стул',
        'discounts': 'горячее предложение',
        'price': '2585.9',
    }
    return  render(request, 'mainapp/products.html', contex)
