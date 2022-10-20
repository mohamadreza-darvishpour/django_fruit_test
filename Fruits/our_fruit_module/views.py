from django.shortcuts import render
from django.http import HttpResponse 
from .models import fruit
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views import View

def one(request):
    data = fruit.objects.all()
    dict = {'fruits': data,
            'test':data[0],
        }
    # return HttpResponse("hey you start godly.")
    return render(request,'our_fruit_module/fruit.html',dict)
   
   
   
class FruitListView(TemplateView):
    template_name = 'our_fruit_module/fruit.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fruits'] = fruit.objects.all()
        print(context['fruits'])
        return context
   
# class FruitListView(ListView):
#     model = fruit
#     template_name = 'our_fruit_module/fruit.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['fruits'] = fruit.objects.all()
#         print(context['fruits'])
#         return context