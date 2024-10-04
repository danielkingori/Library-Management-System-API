from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from django.conf import settings


#fetch user model
User = get_user_model()

class UserRegistrationView(generics.CreateAPIView):
    #retrieves all user records
    queryset = User.objects.all()
    #associates the view with the serializer
    serializer_class = UserRegistrationSerializer

