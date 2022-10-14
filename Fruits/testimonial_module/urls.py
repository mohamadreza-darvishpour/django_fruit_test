from django.urls import URLPattern, path,include 
from . import views 
urlpatterns = [
    path('one/'  , views.one     , name = 'test_one'  ),
]