from django.urls import path, include
from .views import UserRegistrationViewSet, UserLoginViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'register', UserRegistrationViewSet, basename='register')
router.register(r'login', UserLoginViewSet, basename='login')

urlpatterns = [
    path('', include(router.urls)),
]

# from django.urls import path
# from .views import UserRegistrationView, UserLoginSerializer

# urlpatterns = [
#     path('register/', UserRegistrationView.as_view(), name='register'),
#     path('login/', UserLoginSerializer, name='login'),
   
# ]
