from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from django.contrib.auth.models import User

from amountspend.forms import AmountSpendForm
from amountspend.models import AmountSpend


class amountspend(TemplateView):
    template_name = 'amountspend/amountspend.html'
    
    def get(self, request):
        form = AmountSpendForm()
        amountspends = AmountSpend.objects.all()

        args = {'form':form,'amountspends':amountspends}
        return render(request, self.template_name,args)

    def post(self, request):
        form = AmountSpendForm(request.POST)
        if form.is_valid():
            amountspend = form.save(commit=False)
            amountspend.user = request.user
            amountspend.save()
            text = form.cleaned_data['amountspend']
            amount = form.cleaned_data['amount']
            form = AmountSpendForm()
            return redirect('amountspend:amountspend')

        args={'form':form,'text':text}
        return render(request, self.template_name,args)
        

def delete_amountspend(request, pk):
    query = AmountSpend.objects.get(pk=pk)
    remove = AmountSpend.objects.filter(id=pk)
    remove.delete()
    return redirect('amountspend:amountspend')