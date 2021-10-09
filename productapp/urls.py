from django.urls import path
from . import views

app_name = 'productapp'

urlpatterns = [
    path('<int:pk>/', views.ProductDetail.as_view(), name="detail"),
    path('', views.ProductList.as_view(), name="list"),
]