from django.db import models
# Create your models here.
class Match(models.Model):
	img1=models.ImageField(upload_to='images/')
	img2=models.ImageField(upload_to='images/')