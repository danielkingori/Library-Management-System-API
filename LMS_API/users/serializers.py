from rest_framework import serializers
from .models import CustomUser
from django.utils import timezone



#user registration serializer
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'date_of_membership', 'is_active']
    
    def create(self, validated_data):
        #default to noww 
        validated_data['date_of_membership'] = timezone.now()
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            date_of_membership=validated_data['date_of_membership'],
            #default to true
            is_active=validated_data.get('is_active', True),
            
        )
        user.save()
        return user


