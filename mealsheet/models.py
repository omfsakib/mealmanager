from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meal(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    meal = models.IntegerField(default=0)