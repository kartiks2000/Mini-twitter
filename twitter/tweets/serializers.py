from django.contrib.auth import models
from rest_framework import serializers

from .models import Tweet
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    '''Serializes the user objects.'''
    class Meta:
        model = User
        fields = ['username']       

class TweetSerializer(serializers.ModelSerializer):
    '''Serializes the Tweet objetcs'''

    user = UserSerializer()

    class Meta:
        model = Tweet
        fields = ['user','id','content','created']

    def validate_content(self,value):
        if len(value) > 140:
            raise serializers.ValidationError("Too Long!!")
        return value    


