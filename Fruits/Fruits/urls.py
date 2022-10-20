"""Fruits URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home_module.urls')),
    path('about/', include('about_module.urls')),                                                    
    path('ourfruit/', include('our_fruit_module.urls')),   
    path('register/', include('register_module.urls')),     
    path('testimonial/', include('testimonial_module.urls')),    
    path('contactus/', include('contact_us_module.urls')),   
    path('addition/',include('addition.urls')),
 
]


urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
