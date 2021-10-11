# from django.contrib.auth.forms import UserCreationForm
#
# from accountapp.models import User
#
#
# def signup(request):
#     if request.method == 'POST':
#         if request.POST['password1'] == request.POST['password2']:
#             user = User.objects.create_user(
#                 user_id=request.POST['user_id'],
#                 password=request.POST''
#             )
from django.forms import ModelForm

from accountapp.models import User


class UserCreationForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'id', 'address', 'password']