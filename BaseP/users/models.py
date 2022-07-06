import django
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,related_name='user_profile')
    phone = models.CharField(max_length=20, blank=True, null=True)
    passport_img= models.ImageField(upload_to='costumer_profile', default='default.jpg')
