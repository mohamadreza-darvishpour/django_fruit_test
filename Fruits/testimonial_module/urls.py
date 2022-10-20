from django.urls import URLPattern, path,include 
from . import views 
urlpatterns = [
    path('two/'  , views.two.as_view()     , name = 'test_two'  ),
    path('one/'  , views.one     , name = 'test_one'  ),
]