from django import forms
from mealsheet.models import Meal

class MealSheetForm(forms.ModelForm):
    meal = forms.IntegerField()

    class Meta:
        model = Meal
        fields = ('meal',)
