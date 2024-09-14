from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serailizers import UserSerializer
from .models import MyUser
from rest_framework.permissions import AllowAny
from rest_framework.decorators import authentication_classes, permission_classes



# Create your views here.

class UserRegistrationView(generics.CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    
class UserLoginView(APIView):
    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            Token, created = Token.objects.get_or_create(user=user)
            return Response({'token': Token.key})
        else:
            return Response({'error': 'Invalid username or password'}, status=401)
