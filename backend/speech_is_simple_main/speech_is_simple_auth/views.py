import json
from django.http import JsonResponse
from django.shortcuts import redirect, render
from rest_framework.views import APIView
from django.middleware.csrf import rotate_token
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import PatientSerializer, SpecialistPatientSerializer, SpecialistSerializer, UserSerializer
from .models import Patient, Specialist, SpecialistPatient, User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
import jwt, datetime
from django.views.decorators.http import require_POST
from django.middleware.csrf import get_token


def get_csrf(request):
    response = JsonResponse({'detail': 'CSRF cookie set'})
    response['X-CSRFToken'] = get_token(request)
    return response


# @require_POST
# def login_view(request):
#     data = json.loads(request.body)
#     username = data.get('username')
#     password = data.get('password')

#     if username is None or password is None:
#         return JsonResponse({'detail': 'Please provide username and password.'}, status=400)

#     user = authenticate(username=username, password=password)

#     if user is None:
#         return JsonResponse({'detail': 'Invalid credentials.'}, status=400)

#     login(request, user)
#     return JsonResponse({'detail': 'Successfully logged in.'})


# def logout_view(request):
#     if not request.user.is_authenticated:
#         return JsonResponse({'detail': 'You\'re not logged in.'}, status=400)

#     logout(request)
#     return JsonResponse({'detail': 'Successfully logged out.'})


@ensure_csrf_cookie
def session_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({'isAuthenticated': False})

    return JsonResponse({'isAuthenticated': True})


def whoami_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({'isAuthenticated': False})

    return JsonResponse({'username': request.user.username})

class PatientRegisterView(APIView):
    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(validated_data=request.data)
        return Response({
            "message": "success"
        })
    
class SpecialistRegisterView(APIView):
    def post(self, request):
        serializer = SpecialistSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(validated_data=request.data)
        return Response({
            "message": "success"
        })

@method_decorator(ensure_csrf_cookie, name='dispatch')
class LoginView(APIView):
    def post(self, request):
        data = json.loads(request.body)
        username = data.get('email')
        password = data.get('password')
        
        if username is None or password is None:
            return JsonResponse({'detail': 'Please provide username and password.'}, status=400)
        
        user = authenticate(username=username, password=password)
        if user is None:
            return JsonResponse({'detail': 'Invalid credentials.'}, status=400)
        
        login(request, user)
        return JsonResponse({'detail': 'Successfully logged in.', 'type': user.type})
        # email = request.data['email']
        # password = request.data['password']
        # user = authenticate(request, username=email, password=password)
        
        # if user is not None:
        #     login(request, user)
        #     serializer = UserSerializer(User.objects.filter(id=user.id).first())

        # else:
        #     raise AuthenticationFailed('Unauthenticated')
        
        # return Response(serializer.data)
    

        # payload = {
        #     "id": user.id,
        #     "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=60),
        #     "iat": datetime.datetime.now(datetime.UTC)
        # }

        # token = jwt.encode(payload, 'secret', algorithm='HS256')

        # response = Response()

        # response.set_cookie(key='jwt', value=token, httponly=True)
        # response.set_cookie(key='type', value=user.type, httponly=True)
        # response.set_cookie(key='id', value=user.id, httponly=False)

        # response.data = {
        #     'jwt': token,
        #     'type': user.type,
        #     'id': user.id
        # }

        # return response

# class UserView(APIView):
#     def get(self, request):
#         token = request.COOKIES.get('jwt')

#         if not token:
#             raise AuthenticationFailed('Unauthenticated')
        
#         try:
#             payload = jwt.decode(token, 'secret', algorithms=['HS256'])
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed('Unauthenticated')
        
#         user = User.objects.filter(id=payload['id']).first()
#         if (user.type == "SPECIALIST"):
#             serializer = SpecialistSerializer(Specialist.objects.filter(id=payload['id']).first())
#         elif (user.type == "PATIENT"):
#             serializer = PatientSerializer(Patient.objects.filter(id=payload['id']).first())
        
#         return Response(serializer.data)

@method_decorator(ensure_csrf_cookie, name='dispatch')
class LogoutView(APIView):
    def post(self, request):
    #     logout(request)
        if not request.user.is_authenticated:
            return JsonResponse({'detail': 'You\'re not logged in.'}, status=400)

        logout(request)
        return JsonResponse({'detail': 'Successfully logged out.'})
    
        # response.delete_cookie('jwt')
        # response.delete_cookie('type')
        # response.delete_cookie('id')
        # response.data = {
        #     'message': 'success'
        # }
        # return response

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




    