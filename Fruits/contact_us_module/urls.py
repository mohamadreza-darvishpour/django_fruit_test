from django.urls import URLPattern, path,include 
from . import views 
urlpatterns = [
    path('one/'  , views.one     , name = 'contact_one'  ),
]