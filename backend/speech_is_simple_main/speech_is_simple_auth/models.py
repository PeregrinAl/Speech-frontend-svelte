from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=255, default='ANONYMUS')
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Specialist(User):
    is_verified = models.BooleanField(default=True) # TODO: ОПАСНО

class Patient(User):
    date_of_birth = models.DateField()

# SpecialistPatient

# TODO
class SpecialistPatient(models.Model):
    patient = models.ForeignKey(Patient, on_delete = models.PROTECT)
    specialist = models.ForeignKey(Specialist, on_delete = models.PROTECT)
