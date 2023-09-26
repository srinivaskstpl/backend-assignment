# api/urls.py

# django imports
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

# local imports
from api import views

urlpatterns = [
    path("register/", views.UserRegistrationView.as_view(), name="user-registration"),
    path("login/", jwt_views.TokenObtainPairView.as_view(), name="login-view"),
    path("user-profiles/", views.UserProfileView.as_view(), name="user-profile"),
    path("post/create/", views.PostCreateView.as_view(), name="post-create"),
    path("post/list/", views.PostListView.as_view(), name="post-list"),
    path("follower/create/", views.CreateUserFollower.as_view(), name="add-follower"),
]
