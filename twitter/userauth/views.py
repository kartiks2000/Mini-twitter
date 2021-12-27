from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view


from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login


@api_view(['POST','GET'])
def user_login(request,username,password):
    '''Logs in the existing user.
        :param username: username
        :param password: password
    '''

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request,user)
    else:
        return HttpResponse("<h1>wrong credentials!!</h1>")   

    return HttpResponse("<h1>Welcome back</h1>")


@api_view(['POST','GET'])
def user_signup(request,username,password,email):
    '''Creates new user.
        :param username: username
        :param password: password
        :param email: email
    '''

    # Checking if username already exists   
    user = User.objects.filter(username = username)

    if user.exists():
        return HttpResponse("<h1>Username already exists!!!!</h1>")  

    # Creating a new user
    new_user = User.objects.create_user(username=username,password=password,email=email)
    new_user.save()

    return HttpResponse("<h1>Glad to have you on board!!</h1>")


@api_view(['POST','GET'])
def user_logout(request):
    '''Logs out the currently loggedin user.'''
    
    logout(request)

    return HttpResponse("<h1>Logged out!!!</h1>")
