
from django.urls import path,include
from .views import UserRegistrationView,UserLoginView,UserProfileView,UserChangePassword,SendPasswordResetEmailView,UserPasswordResetView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(),name='register'),
    path('login/', UserLoginView.as_view(),name='login'),
    path('profile/', UserProfileView.as_view(),name='login'),
    path('password/', UserChangePassword.as_view(),name='login'),
    path('rest-password/',SendPasswordResetEmailView.as_view(),name='rest-password'),
    
    path('reset-password/<uid>/<token>/',UserPasswordResetView.as_view(),name='reset-password'),
         
     
]

