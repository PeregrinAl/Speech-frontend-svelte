from django.urls import path, include 
from .views import PatientRegisterView, SpecialistRegisterView, LoginView, LogoutView, AddUserView, getPatientsView, get_csrf, session_view, whoami_view
urlpatterns = [
    path('patientregister', PatientRegisterView.as_view()),
    path('specialistregister', SpecialistRegisterView.as_view()),
    path('login', LoginView.as_view()),
    # path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('addpatient', AddUserView.as_view()),
    path('getpatients', getPatientsView.as_view()),
    path('csrf', get_csrf, name='api-csrf'),
    path('session', session_view, name='api-session'),
    path('whoami', whoami_view, name='api-whoami'),
]