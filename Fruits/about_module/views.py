from http.client import ImproperConnectionState, ResponseNotReady
from django.shortcuts import render
from django.http import HttpResponse 



def one(request):
    return HttpResponse("hey you start godly.")


