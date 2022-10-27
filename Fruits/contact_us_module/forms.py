from django.forms import Form ,ModelForm 
from django.contrib.auth.models import User
from django import forms 
class UserModelForm(ModelForm):
    confirm_password = forms.CharField()
    class Meta:
        model = User
        fields = ['username','email','password']
        