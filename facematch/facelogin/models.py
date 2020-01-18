from django.db import models
from django.contrib.auth.models import User
from PIL import Image
 # needed to show the right widget in the admin

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField( upload_to='images')
    temp=models.ImageField(upload_to='login',default='login/default.png')
    def __str__(self):
    	return f'{self.user.username} Profile'


    def save(self,*args,**kwargs):
    	super().save(*args,**kwargs)
    	img=Image.open(self.image.path)

    	if img.height>300 or img.width>300:
    		output_size=(300,300)
    		img.thumbnail(output_size)
    		img.save(self.image.path)


    def save(self):
        super().save()
        img=Image.open(self.temp.path)
        img = img.convert('RGB')
        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
