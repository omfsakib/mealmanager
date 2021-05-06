from django.urls import path
from mealsheet.views import mealsheet
from . import views

app_name = 'mealsheet'

urlpatterns = [
    path('',mealsheet.as_view(),name='mealsheet'),
    path('delete_meal/<int:pk>/',views.delete_meal, name='delete_meal')
]
