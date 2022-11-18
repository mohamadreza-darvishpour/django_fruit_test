from django.forms import ModelForm 
from .models import RequestCall
from django.contrib.auth.models import User
from django import forms 







class UserModelForm(ModelForm):
    confirm_password = forms.CharField()
    class Meta:
        model = User
        fields = ['username','email','password']
        


class RequestCall(forms.Form):
   class Meta:
        model = RequestCall
        fields = ['full_name' , 'email'  , 'phone_number' , 'message' ]


