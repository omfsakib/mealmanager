from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from django.contrib.auth.models import User

from messdetails.forms import MessNameForm
from messdetails.models import MessName
from groups.models import Friend

class messdetails(TemplateView):
    template_name = 'messdetails/messdetails.html'

    def get(self, request):
        form = MessNameForm(request.POST)
        messnames = MessName.objects.all()
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()

        args = {'form':form,'friends':friends}
        return render(request, self.template_name,args)

    def post(self, request):
        form = MessNameForm(request.POST)
        if form.is_valid():
            messname = form.save(commit=False)
            messname.user = request.user
            messname.save()
            text = form.cleaned_data['messname']
            form = MessNameForm()
            return redirect('messdetails:messdetails')

        args={'form':form,'text':text}
        return render(request, self.template_name,args)

        