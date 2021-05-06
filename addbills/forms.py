from django import forms
from addbills.models import Bill

class AddbillsForm(forms.ModelForm):
    bill = forms.CharField()
    amount = forms.IntegerField()

    class Meta:
        model = Bill
        fields = ('bill','amount')
