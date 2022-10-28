from django.urls import URLPattern, path,include 
from . import views 


urlpatterns = [
    path('one/'  , views.ContactUsFormView.as_view()     , name = 'contact_one'  ),
    # path('one/'  , views.one     , name = 'contact_one'  ),
]