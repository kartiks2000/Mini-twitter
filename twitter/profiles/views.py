from rest_framework import serializers
from rest_framework.response import Response
from django.http import Http404, response
from rest_framework.decorators import api_view, permission_classes, authentication_classes

from rest_framework.permissions import IsAuthenticated

from .models import Profile

from django.contrib.auth.models import User

from .serializer import ProfileSerializer

@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def allprofiles(request):
    """Returns all the profiles."""
    qs = Profile.objects.all()

    serializer = ProfileSerializer(qs,many=True)

    print(qs)
    return Response(serializer.data)

@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def profile_detail(request,username):
    """Returns the profile of the username given.
        :param username: the user for which profile has to be fetched.
    """
    qs = Profile.objects.filter(user__username = username)

    if not qs.exists():
        raise Http404

    profile_obj = qs.first()
    serializer = ProfileSerializer(profile_obj)
    print(profile_obj.bio)

    return Response(serializer.data)


@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def current_user_profile(request):
    '''Returns profile of current user.'''

    me_qs = Profile.objects.filter(user = request.user)

    if not me_qs.exists():
        raise Http404
    
    me = me_qs.first()
    serializer = ProfileSerializer(me)

    return Response(serializer.data)


@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def follow_unfollow_profiles(request,username,action):
    """follows and unfollows users
        :params action: Either FOLLOW or UNFOLLOW
        :params username: profile to follow or unfollow
    """

    qs = User.objects.filter(username = username)

    if not qs.exists():
        raise response({},status=404)

    me = request.user

    qs = qs.first()
    me_profile = me.profile
    
    if action == "follow" and me not in me_profile.following.all():
        me_profile.following.add(qs) 
    elif action == "unfollow" and me in me_profile.following.all():
        me_profile.following.remove(qs)  

    return Response({},status=200)     

        