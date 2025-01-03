from django.urls import path
from .views import UserRegistrationView, LoginView, ExampleProtectedView, UserProfileView
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import UserViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('protected/', ExampleProtectedView.as_view(), name='protected'),
    path('profile/', UserProfileView.as_view(), name='profile'),

     # Endpoint to API Views
    path('api-register/', views.RegistrationAPIView.as_view(), name='api-register'),
    path('api-login/', views.LoginAPIView.as_view(), name='api-login'),
    path('api-token-auth/', ObtainAuthToken.as_view(), name='api-token-auth'),
    path('follow/<int:user_id>/', views.FollowUser.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', views.UnfollowUser.as_view(), name='unfollow-user'),
]
