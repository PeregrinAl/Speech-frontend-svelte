from rest_framework import serializers
from .models import Patient, Specialist, SpecialistPatient, User

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'email', 'type','password', 'date_of_birth']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
class SpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = ['first_name', 'last_name', 'email', 'type', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
class SpecialistPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialistPatient
        fields = ['specialistId', 'patientId']

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance
    

