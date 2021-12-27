from django.urls import path

from .views import profile_detail, allprofiles, follow_unfollow_profiles, current_user_profile

# BASE "api/profiles/"

urlpatterns = [
    path('profile/<str:username>',profile_detail),
    path('allprofiles',allprofiles),
    path('currentprofile',current_user_profile),
    path('follow_unfollow/<str:username>/<str:action>',follow_unfollow_profiles),
]
