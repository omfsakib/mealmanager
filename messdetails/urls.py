from django.urls import path
from messdetails.views import messdetails
from. import views

app_name = 'messdetails'

urlpatterns = [
    path('',messdetails.as_view(),name='messdetails'),
]
