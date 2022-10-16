from django import views
from django.shortcuts import render
from django.template import TemplateSyntaxError
from django.views.generic.base import TemplateView
# Create your views here.


class   HeaderNavPartial(TemplateView):
    template_name = 'addition/headerpartial.html'

    #def getcontextdata


class   FooterPartial(TemplateView):
    template_name = 'addition/footer_partial.html'
    