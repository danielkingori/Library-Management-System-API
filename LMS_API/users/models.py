from django.db import models
from django.contrib.auth.models import AbstractUser


#extending to django-buit-in User model
class CustomUser(AbstractUser):
    ADMIN = 'admin'
    MEMBER = 'member'
    
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (MEMBER, 'Member'),
    ]
    # Date of Membership
    date_of_membership = models.DateField(auto_now_add=True) 
    
    # Role (Admin or Member)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=MEMBER)
    # Active Status
    is_active = models.BooleanField(default=True)              

    def __str__(self):
        return self.username
    
