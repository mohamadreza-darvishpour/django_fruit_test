from django.urls import URLPattern, path,include 
from . import views 
urlpatterns = [
    path('two/'  , views.two.as_view()     , name = 'test_one'  ),
    path('one/'  , views.one     , name = 'test_two'  ),
]