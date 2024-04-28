from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from .models import SpecialistPatient

class AddUserView(APIView):
    def post(self, request):
        # TODO: проверить
        patientId = request.data['patientId']
        specialistId = request.data['password']

        token = request.COOKIES.get('jwt')

        response = Response()

        if not token:
            raise AuthenticationFailed('Unauthenticated')
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        
        relation = SpecialistPatient.objects.filter(id=payload['patientId']).first()
        if relation is None:
            SpecialistPatient.objects.create(patientId=patientId, specialistId=specialistId)
            response.data = {
                'message': 'success'
            }
        else:
            response.data = {
                'message': 'already exist'
            }

        return response
