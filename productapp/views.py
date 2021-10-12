from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from productapp.forms import ProductCreationForm
from productapp.models import Product, Category


class ProductList(ListView):
    model = Product
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context


class ProductDetail(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductCreationForm
    template_name = 'productapp/create.html'
    # model.category_id = 2
    # def form_valid(self, form):
    #     form.instance.writer = self.request.user
    #     return super().form_valid(form)

    def get_success_url(self):
        # writer = self.request.user
        # writer.profile.mileage += 10
        # writer.profile.save()
        return reverse('productapp:list')
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

def category_page(request, slug):
    category = Category.objects.get(slug=slug)
    product_list = Product.objects.filter(category=category)

    return render(
        request,
        'productapp/product_list.html',
        {
            'product_list':product_list,
            'categories':Category.objects.all(),
            'category':category,
        }
    )