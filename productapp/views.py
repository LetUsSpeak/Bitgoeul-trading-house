from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from productapp.models import Product


class ProductList(ListView):
    model = Product
    ordering = '-pk'

class ProductDetail(DetailView):
    model = Product


# def index(request):
#     # 가장 최근에 등록된 상품부터 나열
#     products = Product.objects.all().order_by('-pk')
#
#     return render(
#         request,
#         'productapp/product_list.html',
#         {
#             'products': products,
#         }
#     )

# def single_product_page(request, pk):
#     product = Product.objects.get(pk=pk)
#
#     return render(
#         request,
#         'productapp/product_detail.html',
#         {
#             'product': product,
#         }
#     )