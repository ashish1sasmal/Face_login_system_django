from django.db import models
from django.contrib.auth.models import User

 # needed to show the right widget in the admin

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField( upload_to='images')

    def __str__(self):
    	return f'{self.user.username} Profile'

class Snaps(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='login')
