from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Profile


class UserSerializer(serializers.ModelSerializer):
    '''Serializes the user object.'''
    class Meta:
        model = User
        fields = ['username']  

class ProfileSerializer(serializers.ModelSerializer):
    '''Serializes the Profile objects.'''

    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ['user','id','bio','location']