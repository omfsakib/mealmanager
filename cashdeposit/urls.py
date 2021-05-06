from django.urls import path
from cashdeposit.views import cashdeposit
from. import views

app_name = 'cashdeposit'

urlpatterns = [
    path('',cashdeposit.as_view(),name='cashdeposit'),
    path('delete_cashdeposit/<int:pk>/',views.delete_cashdeposit, name='delete_cashdeposit')
]
