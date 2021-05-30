from django.db import models
from django.contrib.auth.models import User
from accounts.forms import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    description = models.CharField(max_length=500,default='')
    city = models.CharField(max_length=100,default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    profession = models.CharField(max_length=100,default='')
    institute = models.CharField(max_length=100,default='')
    blood = models.CharField(max_length=10,default='')
    
    image = models.ImageField(upload_to='profile_image',default='default.jpg')

    def __str__(self):
        return self.user.username

def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)
