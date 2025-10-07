from django.urls import path
from .views import RegisterView, ProfileView
from rest_framework.authtoken.views import obtain_auth_token
from .views import follow_user, unfollow_user

urlpatterns = [
    path('register/', RegisterView.as_view(), name='api-register'),
    path('login/', obtain_auth_token, name='api-login'),   # POST username & password -> token
    path('profile/', ProfileView.as_view(), name='api-profile'),
    path('follow/<int:user_id>/', follow_user, name='follow-user'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow-user'),
]
