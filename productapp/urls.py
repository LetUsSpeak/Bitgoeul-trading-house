from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.single_product_page),
    path('', views.ProductList.as_view()),
]