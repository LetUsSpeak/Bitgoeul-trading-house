from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from productapp.models import Product


# class ProductList(ListView):
#     model = Product

def index(request):
    # 가장 최근에 등록된 상품부터 나열
    products = Product.objects.all().order_by('-pk')

    return render(
        request,
        'productapp/index.html',
        {
            'products': products,
        }
    )