# Mini-twitter


### A social media service build using django.

## Features of the app

The features emplimented are -:

1. Authetication
1. Creating new tweet
1. Deleting tweet
1. Display Feed
1. Follow other users
2. Unfollow users


## Install virtualenv

    python3 -m pip install --user virtualenv
    
## Create virtual Environment

    virtualenv --python=python3 venv    
    
## Activate virtual Environment

    source venv/bin/activate 
    
## Install dependencies from requirements.txt

    pip3 install -r requirements.txt 
    
## Change directory to django_API, and run server

    python3 manage.py runserver 
    
    
### Congrats, you are good to go. Your local server is running and are ready to accept you API calls at:

    http://127.0.0.1:8000/
    
    
## BASE = http://127.0.0.1:8000/api/

### Auth “auth/“

# Signup “signup/<str:username>/<str:password>/<str:email>”
## Signing in as a new user.

# Login “login/<str:username>/<str:password>”
## Logging in the existing user.

Logout “signup/<str:username>/<str:password>/<str:email>”
Logout the currently logged in user.


Tweets   “tweets/”

Create Tweet “create/<str:tweet_content>”
Creates a new tweet for the currently logged in user.

Delete Tweet “delete/<int:tweet_id>”
Deleted the tweet mentioned by the user if and only if the tweet belongs to the currently logged in user.

Specific tweet “tweet/<int:tweet_id>”
Shows content of a specific tweet.

All tweets of current user “alltweetsofuser”
Returns all the tweets of the current user.

All tweets “alltweets“
Returns the tweets of all the users on the platform.

Feed “feed”
Return tweets of currently logged in users and the followed users.


Profiles “profiles/“

Specific user profile “profile/<str:username>”
Shows the profile of currently logged in user

All users/profile “allprofiles”
Returns all the users on the platform

Followed users “followedusers”
Returns all the followed users.

Currently logged in user “currentprofile”
Returns the currently logged in user profile

Follow user “follow_unfollow/<str:username>/follow”
Follow the specific user.

Follow user “follow_unfollow/<str:username>/unfollow”
Unfollow the specific user.
    
    
    
# THANKS & REGARDS    
