# # # from django.contrib.auth.forms import UserCreationForm
# # # from django.contrib.auth.models import User
# # # from django.shortcuts import render
# # #
# # # # Create your views here.
# # # from django.urls import reverse
# # # from django.views.generic import CreateView
# # #
# # #
# # # class AccountCreateView(CreateView):
# # #     model = User
# # #     form_class = UserCreationForm
# # #     template_name = 'accountapp/create.html'
# # #
# # #     def get_success_url(self):
# # #         return reverse('marketapp:main')
# # from django.contrib import auth
# # from django.contrib.auth import authenticate
# # # from django.contrib.auth.models import User
# # from django.shortcuts import render, redirect
# #
# #
# # # Create your views here.
# # # 회원가입
# # from accountapp.models import User
# #
# #
# # def signup(request):
# #     if request.method == 'POST':
# #         if request.POST['password1'] == request.POST['password2']:
# #             user = User.objects.create_user(
# #                                                 id=request.POST['id'],
# #                                                 username=request.POST['username'],
# #                                                 password=request.POST['password1'],
# #                                                 address=request.POST['address'], )
# #             auth.login(request, user)
# #             return redirect('/')
# #         return render(request, 'accountapp/create.html')
# #     return render(request, 'accountapp/create.html')
# from django.shortcuts import render
# from django.http import HttpResponse
# from django.contrib.auth.hashers import make_password
# from .models import User
# # Create your views here.
# def create(request):   #회원가입 페이지를 보여주기 위한 함수
#     if request.method == "GET":
#         return render(request, 'marketapp/metaverse.html')
#
#     elif request.method == "POST":
#         username = request.POST['username']   #딕셔너리형태
#         id = request.POST['id']
#         address = request.POST['address']
#         password = request.POST['password']
#         re_password = request.POST['re_password']
#         res_data = {}
#         if not (username or id or address or password or re_password):
#             res_data['error'] = "모든 값을 입력해야 합니다."
#         if password != re_password :
#             # return HttpResponse('비밀번호가 다릅니다.')
#             res_data['error'] = '비밀번호가 다릅니다.'
#         else :
#             user = User(username=username, id=id, address=address, password=make_password(password))
#             user.save()
#         return render(request, 'marketapp/metaverse.html', res_data) #register를 요청받으면 register.html
from django.urls import reverse
from django.views.generic import CreateView

from accountapp.forms import UserCreationForm
from accountapp.models import User




class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'accountapp/create.html'

    def get_success_url(self):
        return reverse('marketapp:main')