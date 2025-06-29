
from django.urls import path,include
from .views import UserRegistrationView,UserLoginView,UserProfileView,UserChangePassword

urlpatterns = [
    path('register/', UserRegistrationView.as_view(),name='register'),
    path('login/', UserLoginView.as_view(),name='login'),
    path('profile/', UserProfileView.as_view(),name='login'),
    path('password/', UserChangePassword.as_view(),name='login'),
    
    
]