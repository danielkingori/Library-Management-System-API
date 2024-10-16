# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import CustomUser

# # Register CustomUser with UserAdmin
# class CustomUserAdmin(UserAdmin):
#     # Display the role in the admin list view
#     list_display = ('username', 'email', 'role', 'is_active', 'date_of_membership')
#     fieldsets = UserAdmin.fieldsets + (
#         (None, {'fields': ('role', 'date_of_membership', 'is_active')}),
#     )
# admin.site.register(CustomUser,UserAdmin,CustomUserAdmin)

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register CustomUser with UserAdmin
class CustomUserAdmin(UserAdmin):
    # Display the role in the admin list view
    list_display = ('username', 'email', 'role', 'is_active', 'date_of_membership')
    
    # Copy the existing fieldsets and add new fields where necessary
    fieldsets = (
        *UserAdmin.fieldsets,  # Unpack the default fieldsets from UserAdmin
        (None, {'fields': ('role',)}),  # Add your custom fields here
    )

# Register the CustomUser model with CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)

