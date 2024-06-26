from django.forms import ModelForm
from .models import Room , User
from django.contrib.auth.forms import UserCreationForm

class newUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','name','password1','password2']

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host','participants']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','email','name','profile_image','bio']