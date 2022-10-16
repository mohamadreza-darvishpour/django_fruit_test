from django.shortcuts import render
from django.http import HttpResponse 



def one(request):
    #return HttpResponse("hey you start godly.")
    return render(request,'contact_us_module/contact.html')
