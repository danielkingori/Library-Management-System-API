from django.db import models
from django.contrib.auth.models import AbstractUser


#extending to django-buit-in User model
class CustomUser(AbstractUser):
    # Date of Membership
    date_of_membership = models.DateField(auto_now_add=True) 
    # Active Status
    is_active = models.BooleanField(default=True)              

    def __str__(self):
        return self.username
    
