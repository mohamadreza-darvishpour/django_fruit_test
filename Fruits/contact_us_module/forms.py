from django.forms import Form ,ModelForm 
from django.contrib.auth.models import User

class UserModelForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password']