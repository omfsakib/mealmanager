from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from django.contrib.auth.models import User

from cashdeposit.forms import CashDepositForm
from cashdeposit.models import CashDeposit
from groups.models import Friend


class cashdeposit(TemplateView):
    template_name = 'cashdeposit/cashdeposit.html'
    
    def get(self, request):
        form = CashDepositForm()
        cashdeposits = CashDeposit.objects.all()
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()

        args = {'form':form,'cashdeposits':cashdeposits,'friends':friends}
        return render(request, self.template_name,args)

    def post(self, request):
        form = CashDepositForm(request.POST)
        if form.is_valid():
            cashdeposit = form.save(commit=False)
            cashdeposit.save()
            text = form.cleaned_data['cashdeposit']
            cashdeposit.user = form.cleaned_data['user']
            amount = form.cleaned_data['amount']
            form = CashDepositForm()
            return redirect('cashdeposit:cashdeposit')

        args={'form':form,'text':text}
        return render(request, self.template_name,args)
        

def delete_cashdeposit(request, pk):
    query = CashDeposit.objects.get(pk=pk)
    remove = CashDeposit.objects.filter(id=pk)
    remove.delete()
    return redirect('cashdeposit:cashdeposit')