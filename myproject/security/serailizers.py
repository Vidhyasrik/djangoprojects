from rest_framework import serializers
from .models import MyUser
# User, Profile, Post, Comment, Like, Follow

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = MyUser
        extra_kwargs = {'password': {'write_only': True}}
        fields = ['username','first_name', 'last_name', 'email', 'password']
        
    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

