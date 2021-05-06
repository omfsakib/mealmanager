from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bill(models.Model):
    bill = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    amount = models.IntegerField(default=0)