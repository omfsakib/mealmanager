from django.contrib.auth import update_session_auth_hash
from django.shortcuts import redirect,render
from django.urls import reverse
from accounts.forms import EditUserProfileForm, RegistrationForm,EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.
def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)   
        if form.is_valid():
            form.save()
            return redirect('/account')
    else:
        form = RegistrationForm()

    args = {'form':form}
    return render(request,'accounts/register.html',args)


def view_profile(request, pk = None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user':user}
    return render(request,'accounts/profile.html',args)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST,instance=request.user)
        userform = EditUserProfileForm(request.POST,request.FILES,instance=request.user.userprofile)
        if (form and userform).is_valid():
            user = form.save(commit=False)
            user.save()
            user.userprofile = userform.save(commit=False)
            user.userprofile.description = userform.cleaned_data.get("description")
            user.userprofile.phone = userform.cleaned_data.get("phone")
            user.userprofile.city = userform.cleaned_data.get("city")
            user.userprofile.website = userform.cleaned_data.get("website")
            user.userprofile.profession = userform.cleaned_data.get("profession")
            user.userprofile.blood = userform.cleaned_data.get("blood")
            user.userprofile.institute = userform.cleaned_data.get("institute")
            user.userprofile.save()
            return redirect(reverse('accounts:view_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        userform = EditUserProfileForm(instance=request.user.userprofile)

        args = {'form': form,'userform':userform}
        return render(request, 'accounts/edit_profile.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('accouns:view_profile'))
        else:
            return redirect(reverse('accounts:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)

