from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from django.contrib.auth.models import User

from addbills.forms import AddbillsForm
from addbills.models import Bill


class addbills(TemplateView):
    template_name = 'addbills/addbills.html'
    
    def get(self, request):
        form = AddbillsForm()
        bills = Bill.objects.all()

        args = {'form':form,'bills':bills}
        return render(request, self.template_name,args)

    def post(self, request):
        form = AddbillsForm(request.POST)
        if form.is_valid():
            bill = form.save(commit=False)
            bill.user = request.user
            bill.save()
            text = form.cleaned_data['bill']
            amount = form.cleaned_data['amount']
            form = AddbillsForm()
            return redirect('addbills:addbills')

        args={'form':form,'text':text}
        return render(request, self.template_name,args)
        

def delete_bill(request, pk):
    query = Bill.objects.get(pk=pk)
    remove = Bill.objects.filter(id=pk)
    remove.delete()
    return redirect('addbills:addbills')