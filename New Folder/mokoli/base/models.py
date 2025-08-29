from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    role = ('Admin','admin'), ('Client','client'),
    username = models.CharField(unique=True, max_length=50, blank=False)
    phone = models.IntegerField(default=670000000, unique=True, blank=False)
    email = models.EmailField(unique=True, max_length=254, blank=False)
    user_type = models.CharField(choices=role, max_length=50)

    def __str__(self):
        return self.username

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    