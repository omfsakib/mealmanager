from django.views.generic import TemplateView,ListView
from django.shortcuts import render,redirect
from django.contrib.auth.models import User

from groups.models import Friend

class groups(TemplateView):
    template_name = 'groups/groups.html'
    
    def get(self, request):
        users = User.objects.exclude(id=request.user.id)
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()

        args = {'users':users,'friends': friends}
        return render(request, self.template_name,args)

def change_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, friend)
    return redirect('groups:groups')
