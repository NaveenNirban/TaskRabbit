from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from taskbunny.models import Task



class MyUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1','password2')

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"

