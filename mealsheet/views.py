from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from django.contrib.auth.models import User

from mealsheet.forms import MealSheetForm
from mealsheet.models import Meal
from groups.models import Friend


class mealsheet(TemplateView):
    template_name = 'mealsheet/mealsheet.html'
    
    def get(self, request):
        form = MealSheetForm()
        meals = Meal.objects.all()
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()


        args = {'form':form,'friends':friends}
        return render(request, self.template_name,args)

    def post(self, request):
        form = MealSheetForm(request.POST)
        if form.is_valid():
            meal = form.save(commit=False)
            meal.user = request.user
            meal.save()
            text = form.cleaned_data['meal']
            form = MealSheetForm()
            return redirect('mealsheet:mealsheet')

        args={'form':form,'text':text}
        return render(request, self.template_name,args)
        

def delete_meal(request, pk):
    query = Meal.objects.get(pk=pk)
    remove = Meal.objects.filter(id=pk)
    remove.delete()
    return redirect('mealsheet:mealsheet')