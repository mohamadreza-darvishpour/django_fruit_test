from django.urls import URLPattern, path,include 
from . import views 
urlpatterns = [
    path('one/'  , views.FruitListView.as_view()   , name = 'fruit_two'  ),
    path('one/'  , views.one     , name = 'fruit_one'  ),
]