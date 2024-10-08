from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UserRegistrationView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('auth/', TokenObtainPairView.as_view(), name='auth'),
   
]
