from django.urls import path
from .views import RegisterView, ProfileView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', RegisterView.as_view(), name='api-register'),
    path('login/', obtain_auth_token, name='api-login'),   # POST username & password -> token
    path('profile/', ProfileView.as_view(), name='api-profile'),
]
