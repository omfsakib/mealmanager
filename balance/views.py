from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from groups.models import Friend

class balance(TemplateView):
    template_name = 'balance/balance.html'

    def get(self, request):
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()

        args = {'friends':friends}
        return render(request, self.template_name,args)