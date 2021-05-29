from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )
    def save(self, commit = True):
        user = super(RegistrationForm,self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )

class EditUserProfileForm(forms.ModelForm):
    description=forms.CharField(max_length=100,required=False)
    city = forms.CharField(max_length=100,required=False)
    website = forms.URLField(required=False)
    phone = forms.IntegerField(required=False)
    image = forms.FileField(required=None)

    class Meta:
        model = User
        fields = (
            'description',
            'city',
            'website',
            'phone',
            'image'
            
        )