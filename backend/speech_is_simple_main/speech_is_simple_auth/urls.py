from django.urls import path, include 
from .views import PatientRegisterView, SpecialistRegisterView, LoginView, LogoutView, UserView, AddUserView, getPatientsView

urlpatterns = [
    path('patientregister', PatientRegisterView.as_view()),
    path('specialistregister', SpecialistRegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('addpatient', AddUserView.as_view()),
    path('getpatients', getPatientsView.as_view()),
]