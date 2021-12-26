from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication

from rest_framework.permissions import IsAuthenticated

from .models import Tweet
from profiles.models import Profile

from django.contrib.auth.models import User

from .serializers import TweetSerializer

@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def create_tweet(request, tweet_content):

    # serializer = TweetSerializer(data=)
    tweet = Tweet.objects.create(user=request.user,content=tweet_content)

    print(tweet.created)

    return Response("<h1>created!!</h1>")


# All tweets of the current user
@api_view(['GET'])
# @authentication_classes([authentication_classes])
@permission_classes([IsAuthenticated])
def all_tweets_of_current_user(request):
    """Returns all tweets of the currently logged in user."""
    tweet_qs = Tweet.objects.filter(user = request.user)

    serializer = TweetSerializer(tweet_qs,many=True)

    print(tweet_qs,request.user)
    return Response(serializer.data)


# All tweets of all users
@api_view(['GET'])
# @authentication_classes([authentication_classes])
@permission_classes([IsAuthenticated])
def all_tweets(request):
    """Returns all tweets of all the users."""
    
    tweet_qs = Tweet.objects.all()

    serializer = TweetSerializer(tweet_qs,many=True)

    print(tweet_qs,request.user)
    return Response(serializer.data)


@api_view(['GET'])
# @authentication_classes([authentication_classes])
@permission_classes([IsAuthenticated])
def tweet_content(request,tweet_id):
    """Returns a specific tweet.
        :param tweet_id: The ID of the tweet 
    """

    tweet = Tweet.objects.filter(id=tweet_id)

    serializer = TweetSerializer(tweet)

    return Response(serializer.data)


@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def show_feed(request):
    """Shows all the tweets by the user and the followed users."""   

    # Current users posts
    me_tweets_qs = Tweet.objects.filter(user = request.user)

    # followed user posts
    other_user_tweet_qs = Tweet.objects.filter(user__in = request.user.profile.following.all())

    # merging both querysets
    final_qs = me_tweets_qs | other_user_tweet_qs  

    # Sorting the tweets    
    final_qs = final_qs.order_by('-created')

    serializer = TweetSerializer(final_qs,many=True)


    return Response(serializer.data)


@api_view(['POST','GET','DELETE'])
@permission_classes([IsAuthenticated])
def delete_tweet(request, tweet_id):
    """Deletes a specific tweet.
        :param tweet_id: The ID of the tweet
    """

    # Extracting the tweet
    tweet_qs = Tweet.objects.filter(id=tweet_id)   

    # Verifing if the tweet exist
    if not tweet_qs.exists():
        return Response({"msg":"tweet not found!!!"},status = 400) 

    # If the tweet belong to the logged in user
    qs = tweet_qs.filter(user=request.user)

    if not qs.exists():
        return Response({"message":"permission denied"})

    tweet_obj = qs.first()
    tweet_obj.delete()

    return Response({"msg":"Deleted!!"})
