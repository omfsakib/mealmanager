from django.shortcuts import redirect,render,HttpResponse
from django.urls import reverse
from accounts.forms import RegistrationForm,EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.
def home(request):
    return HttpResponse('It Works !')


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
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.userprofile.description = form.cleaned_data['description']
            user.userprofile.phone = form.cleaned_data['phone']
            user.userprofile.city = form.cleaned_data['city']
            user.userprofile.website = form.cleaned_data['website']
            user.userprofile.image = form.cleaned_data['image']
            return redirect(reverse('accounts:view_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
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

