from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    type = models.CharField(max_length=255, default='ANONYMUS')
    password = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Specialist(User):
    pass

class Patient(User):
    date_of_birth = models.DateField()

