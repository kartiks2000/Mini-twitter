from django.urls import path

from .views import user_logout, user_login, user_signup

# BASE "api/auth/"

urlpatterns = [
    path('logout',user_logout),
    path('login/<str:username>/<str:password>',user_login),
    path('signup/<str:username>/<str:password>/<str:email>',user_signup),
]