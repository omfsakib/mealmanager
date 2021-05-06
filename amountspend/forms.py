from django import forms
from amountspend.models import AmountSpend

class AmountSpendForm(forms.ModelForm):
    amountspend = forms.CharField()
    amount = forms.IntegerField()

    class Meta:
        model = AmountSpend
        fields = ('amountspend','amount')
