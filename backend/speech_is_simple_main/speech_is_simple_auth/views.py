from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import PatientSerializer, SpecialistPatientSerializer, SpecialistSerializer
from .models import Patient, Specialist, SpecialistPatient, User
import jwt, datetime

class PatientRegisterView(APIView):
    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class SpecialistRegisterView(APIView):
    def post(self, request):
        serializer = SpecialistSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')
        
        payload = {
            "id": user.id,
            "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=60),
            "iat": datetime.datetime.now(datetime.UTC)
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.set_cookie(key='type', value=user.type, httponly=True)
        response.set_cookie(key='id', value=user.id, httponly=False)

        response.data = {
            'jwt': token,
            'type': user.type,
            'id': user.id
        }

        return response

class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated')
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        
        user = User.objects.filter(id=payload['id']).first()
        if (user.type == "SPECIALIST"):
            serializer = SpecialistSerializer(Specialist.objects.filter(id=payload['id']).first())
        elif (user.type == "PATIENT"):
            serializer = PatientSerializer(Patient.objects.filter(id=payload['id']).first())
        
        return Response(serializer.data)
    
class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.delete_cookie('type')
        response.delete_cookie('id')
        response.data = {
            'message': 'success'
        }
        return response

class AddUserView(APIView):
    def post(self, request):
        # TODO: проверить
        patientId = request.data['patientId']
        specialist = request.COOKIES.get('id')
        
        patient = Patient.objects.get(id = patientId)
        specialist = Specialist.objects.get(id = specialist)
        
        response = Response()
        
        relation = SpecialistPatient.objects.filter(specialist=specialist) & SpecialistPatient.objects.filter(patient=patient)
        if not relation:
            SpecialistPatient.objects.create(specialist=specialist, patient = patient)
            response.data = {
                'message': 'success'
            }
        else:
            response.data = {
                'message': relation
            }

        return Response('')
    
class getPatientsView(APIView):
    def get(self, request):
        specialist = request.COOKIES.get('id')
        if True:
            response = Response()
            response.data = {
                'token': request.COOKIES.get('id')
                }
            patients = Patient.objects.filter(specialistpatient__specialist_id=specialist)
            serializer = PatientSerializer(patients, many=True)
            return Response(serializer.data)
        else:
            return Response({'user_id': token})



    