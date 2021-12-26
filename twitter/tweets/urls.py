from django.urls import path

from .views import tweet_content, all_tweets_of_current_user, create_tweet, delete_tweet, all_tweets, show_feed

# BASE "api/tweets/"

urlpatterns = [
    path('tweet/<int:tweet_id>',tweet_content),
    path('alltweetsofuser',all_tweets_of_current_user),
    path('alltweets',all_tweets),
    path('feed',show_feed),
    path('create/<str:tweet_content>',create_tweet),
    path('delete/<int:tweet_id>',delete_tweet)
]
