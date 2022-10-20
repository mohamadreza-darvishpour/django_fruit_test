from django.urls import URLPattern, path,include 
from . import views 
urlpatterns = [
    path('one/'  , views.two.as_view()     , name = 'about_two'  ),
    path('one/'  , views.one     , name = 'about_one'  ),
]