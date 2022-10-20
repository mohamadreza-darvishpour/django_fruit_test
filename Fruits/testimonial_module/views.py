from re import template
from django.shortcuts import render
from django.http import HttpResponse 
from django.views.generic.base import TemplateView
from .models import testimonial

def one(request):
    # return HttpResponse("hey you start godly.")
    return render(request, 'testimonial_module/testimonial.html')



class two(TemplateView):
    template_name = 'testimonial_module/testimonial.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = testimonial.objects.all()
        print(data)
        context['testimonials'] = data
        return context 