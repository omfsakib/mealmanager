from django import forms
from messdetails.models import MessName

class MessNameForm(forms.ModelForm):
    messname = forms.CharField(max_length=100)

    class Meta:
        model = MessName
        fields = ('messname',)
