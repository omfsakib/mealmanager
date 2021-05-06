from django import forms
from cashdeposit.models import CashDeposit

class CashDepositForm(forms.ModelForm):
    cashdeposit = forms.CharField()
    amount = forms.IntegerField()

    class Meta:
        model = CashDeposit
        fields = ('cashdeposit','amount','user')
