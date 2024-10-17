# from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer

#user registration view
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
                
        return Response({
            'user': serializer.data,
        })
