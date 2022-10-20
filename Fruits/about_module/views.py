from http.client import ImproperConnectionState, ResponseNotReady
from re import template
from django.shortcuts import render
from django.http import HttpResponse 
from django.views.generic.base import TemplateView
from .models import about



class two(TemplateView):
    template_name = 'about_module/about.html'
    def get_context_data(self, **kwargs) :
        context =  super().get_context_data(**kwargs)
        data = about.objects.all()
        context['abouts'] = data 
        return context 




def one(request):
    #return HttpResponse("hey you start godly.")
    return render(request,'about_module/about.html')
    

