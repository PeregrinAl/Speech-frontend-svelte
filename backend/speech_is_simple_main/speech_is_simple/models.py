from django.db import models

# SpecialistPatient

# пациент в такой таблице должен фигурировать единожды. Можно ли использовать его как foregin key?
# TODO
class SpecialistPatient(models.Model):
    patientId = models.BigIntegerField()
    specialistId = models.BigIntegerField()

