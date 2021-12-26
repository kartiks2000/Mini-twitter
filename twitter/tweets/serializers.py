from rest_framework import serializers

from .models import Tweet

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['content','created']

    def validate_content(self,value):
        if len(value) > 140:
            raise serializers.ValidationError("Too Long!!")
        return value    