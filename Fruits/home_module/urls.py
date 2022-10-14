from django.urls import URLPattern, path,include 
from . import views 
urlpatterns = [
    path('home/'  , views.one    , name = 'home_one'  ),
]