from django.urls import path
from balance.views import balance
from . import views

app_name = 'balance'

urlpatterns = [
    path('',balance.as_view(),name='balance'),
]