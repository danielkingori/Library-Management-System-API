from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UserRegistrationView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'), #user register, default user role is member, unless super admin selects admin
    path('auth/', TokenObtainPairView.as_view(), name='auth'), #obtain the refresh and access tokens.
   
]
