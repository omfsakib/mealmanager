from django.urls import path
from addbills.views import addbills
from . import views

app_name = 'addbills'

urlpatterns = [
    path('',addbills.as_view(),name='addbills'),
    path('delete_bill/<int:pk>/',views.delete_bill, name='delete_bill')
]
