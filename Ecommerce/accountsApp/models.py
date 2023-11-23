from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.PositiveBigIntegerField(null = False)
    profile_img = models.ImageField(upload_to='photos/accounts', blank=True)

    def __str__(self):
        return self.user.username 
