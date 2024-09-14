from django.urls import path, include
from .views import UserRegistrationView, UserLoginView
urlpatterns = [
    path('user/register', UserRegistrationView.as_view(), name='user_register'),
    path('user/login', UserLoginView.as_view(), name='user_login'),
    

]