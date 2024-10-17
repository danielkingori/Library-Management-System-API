from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Display the role in the admin list view
    list_display = ('username', 'email', 'role', 'is_active', 'date_of_membership')
    
    fieldsets = (
        #Unpack the default fieldsets from UserAdmin
        *UserAdmin.fieldsets,  
        # Add custom field of role, either admin or member
        (None, {'fields': ('role',)}), 
    )

# Register the CustomUser model with CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)

