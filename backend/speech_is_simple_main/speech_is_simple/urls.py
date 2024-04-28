from django.urls import path, include 
from .views import AddUserView

urlpatterns = [
    path('addUser', AddUserView.as_view()),
]