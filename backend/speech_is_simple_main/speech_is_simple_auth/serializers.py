from rest_framework import serializers
from .models import Patient, Specialist, SpecialistPatient, User

    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'type', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        type = validated_data.pop('type', None)
        email = validated_data.pop('email', None)
        instance = self.Meta.model(type=type, username=email)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'date_of_birth', 'user']

    def create(self, validated_data):
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')
        date_of_birth = validated_data.pop('date_of_birth')
        user_object = UserSerializer().create(validated_data.get('user'))
        patient = Patient.objects.create(user=user_object, first_name=first_name, last_name=last_name, date_of_birth=date_of_birth)
        return patient

class SpecialistSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Specialist
        fields = ['first_name', 'last_name', 'is_verified', 'user']

    def create(self, validated_data):
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')
        is_verified = validated_data.pop('is_verified')
        user = UserSerializer().create(validated_data.get('user'))
        specialist = Specialist.objects.create(user=user, first_name=first_name, last_name=last_name, is_verified=is_verified)
        return specialist
    
class SpecialistPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialistPatient
        fields = ['specialistId', 'patientId']

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance
    

