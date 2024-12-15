from django.urls import path
from .views import UserRegistrationView, LoginView, ExampleProtectedView, UserProfileView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('protected/', ExampleProtectedView.as_view(), name='protected'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]
