from django.shortcuts import render
from django.http import HttpResponse 



def one(request):
    #return HttpResponse("hey you start godly.")
    return render(request,'home_module/index.html')