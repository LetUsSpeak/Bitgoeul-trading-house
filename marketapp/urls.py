from django.urls import path
from . import views

app_name = 'marketapp'

urlpatterns = [
    path('', views.landing, name="main"),
    path('metaverse/', views.metaverse, name="metaverse"),
    path('kakao/', views.kakao, name='kakao')
]