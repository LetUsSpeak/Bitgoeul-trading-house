from django.urls import path
from . import views
from .views import ProductCreateView

app_name = 'productapp'

urlpatterns = [
    path('category/<str:slug>/', views.category_page),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name="detail"),
    path('similar/<int:id>', views.similar, name="similar"),
    path('', views.ProductList.as_view(), name="list"),
]