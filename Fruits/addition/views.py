from django import views
from django.shortcuts import render
from django.template import TemplateSyntaxError
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from our_fruit_module.models import fruit
from django.views import View
# Create your views here.


class   HeaderNavPartial(TemplateView):
    template_name = 'addition/headerpartial.html'

    #def getcontextdata


class   FooterPartial(TemplateView):
    template_name = 'addition/footer_partial.html'
    

# class mediatest(View):
#     def get(request):
#         data = fruit.objects.all()
#         dict = {
#             'fruits': data
#         }
#         return render(request,'addition/test.html',dict)