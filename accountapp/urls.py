from django.contrib.auth.views import LoginView
from django.urls import path

from . import views
from .views import UserCreateView

app_name = 'accountapp'

urlpatterns = [
    # path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('create/', UserCreateView.as_view(), name='create'),
]