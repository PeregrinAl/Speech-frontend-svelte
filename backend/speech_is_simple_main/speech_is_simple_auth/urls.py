from django.urls import path, include 
from .views import PatientRegisterView, SpecialistRegisterView, LoginView, LogoutView, UserView

urlpatterns = [
    path('patientRegister', PatientRegisterView.as_view()),
    path('specialistRegister', SpecialistRegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
]