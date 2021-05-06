from django.urls import path
from amountspend.views import amountspend
from . import views

app_name = 'amountspend'

urlpatterns = [
    path('',amountspend.as_view(),name='amountspend'),
    path('delete_amountspend/<int:pk>/',views.delete_amountspend, name='delete_amountspend')
]
