from django.urls import path
from . import views
from .views import ProductCreateView

app_name = 'productapp'

urlpatterns = [
    path('create/', ProductCreateView.as_view(), name='create'),
    path('<int:pk>/', views.ProductDetail.as_view(), name="detail"),
    path('', views.ProductList.as_view(), name="list"),
]