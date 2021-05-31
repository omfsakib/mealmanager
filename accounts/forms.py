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
BLOOD_GROUPS = [
    ('','Choose blood group'),
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('O+', 'O+'),
    ('O-', 'O+'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
]
class EditUserProfileForm(forms.ModelForm):
    description=forms.CharField(required=None,max_length=250,widget=forms.Textarea
                           (attrs={'id':'my-input','placeholder': 'Write about yourself.....','rows':3, 'cols':15}))
    city = forms.CharField(required=None,max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Write your address...'}))
    website = forms.URLField(required=None,widget=forms.TextInput(attrs={'placeholder': 'Enter your Website'}))
    phone = forms.IntegerField(required=None,widget=forms.TextInput(attrs={'placeholder': 'i.e 184644****'}))
    profession = forms.CharField(required=None,max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Write your profession'}))
    blood = forms.CharField(required=None,widget=forms.Select(choices=BLOOD_GROUPS,attrs={'placeholder': 'Choose your blood group'}))
    institute = forms.CharField(required=None,max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Write your institute name'}))

    class Meta:
        model = User
        fields = (
            'description',
            'city',
            'website',
            'phone',
            'profession',
            'blood',
            'institute'
            
        )