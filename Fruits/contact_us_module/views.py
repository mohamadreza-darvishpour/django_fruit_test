from django.shortcuts import render
from django.http import HttpResponse 
from django.views import View

import contact_us_module
from .forms import UserModelForm

def one(request):
    #return HttpResponse("hey you start godly.")
    return render(request,'contact_us_module/contact.html')

class ContactUsFormView(View ):
    def get(self,request):  
        contact_form = UserModelForm()
        dict = {
            'contact_form' : contact_form,
        }
        return render(request , 'contact_us_module/contact.html' , dict )
        


    def post(self,request):
        print('****************************',request.POST['username'],request.POST['email'])
        form = UserModelForm(request.POST)
        
        if  True or request.POST['password'] != request.POST['confirm_password']:
            form.add_error('confirm_password','رمز عبور و تکرار آن برابر نیستند.')
            form.add_error('password','رمز عبور و تکرار آن برابر نیستند.')
        username = request.POST['username']
        dict = {
            'contact_form': form,
        }
        return render(request , 'contact_us_module/contact.html' , dict )









