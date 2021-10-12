from django.urls import path
from . import views

app_name = 'commentapp'

urlpatterns = [
    path('create/', views.create, name='create'),
    path('result/', views.result, name='result')
    # path('result/', views.result, name='result'),
]
