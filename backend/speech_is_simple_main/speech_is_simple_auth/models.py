from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=255, default='ANONYMUS')
    password = models.CharField(max_length=255)

    REQUIRED_FIELDS = []
    
class Specialist(models.Model):
    id = models.BigAutoField(primary_key=True)
    is_verified = models.BooleanField(default=True) # TODO: ОПАСНО
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete = models.PROTECT)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Patient(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    user = models.ForeignKey(User, on_delete = models.PROTECT)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# SpecialistPatient

# TODO
class SpecialistPatient(models.Model):
    patient = models.ForeignKey(Patient, on_delete = models.PROTECT)
    specialist = models.ForeignKey(Specialist, on_delete = models.PROTECT)
