# api/views.py

# third-party imports
from rest_framework import generics, permissions
from rest_framework.response import Response

# local imports
from api.models import Post, User, UserRelationship
from api.serializers import (
    PostListSerializer,
    PostSerializer,
    UserProfileSerializer,
    UserRelationshipSerializer,
    UserSerializer,
)


class UserRegistrationView(generics.CreateAPIView):
    """
    API view for create user accounts
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostListView(generics.ListAPIView):
    """
    API view for list the post's.
    """

    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostCreateView(generics.CreateAPIView):
    """
    API view for creating of a post.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserProfileView(generics.RetrieveAPIView):
    """
    API view to list all user profiles
    """

    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        response = self.get_serializer(request.user).data
        return Response(response)


class CreateUserFollower(generics.CreateAPIView):
    """
    API view to create user followers
    """

    queryset = UserRelationship.objects.all()
    serializer_class = UserRelationshipSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(followed=self.request.user)
