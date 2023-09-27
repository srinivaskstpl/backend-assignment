# api/serializers.py

# third-party imports
from rest_framework import serializers

# local imports
from api.models import Post, User, UserRelationship


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "password",
            "is_staff",
            "is_superuser",
        )

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserRelationshipSerializer(serializers.ModelSerializer):
    follower_name = serializers.CharField(source="follower.full_name", read_only=True)
    followed = serializers.ReadOnlyField(source="followed.id")

    def validate(self, attrs):
        validated_data = super().validate(attrs)
        request_user = self.context.get("request").user

        if UserRelationship.objects.filter(
            followed=request_user, follower=validated_data.get("follower")
        ).exists():
            raise serializers.ValidationError(
                detail="follower already exist.", code="followed"
            )

        return validated_data

    class Meta:
        model = UserRelationship
        fields = "__all__"


class UserProfileSerializer(serializers.ModelSerializer):
    followers_count = serializers.SerializerMethodField()
    followers = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()
    posts = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "followers_count",
            "followers",
            "following_count",
            "posts",
        )

    def get_followers_count(self, obj):
        return UserRelationship.objects.filter(followed=obj).count()

    def get_followers(self, obj):
        followers = UserRelationship.objects.filter(followed=obj)
        return UserRelationshipSerializer(followers, many=True).data

    def get_following_count(self, obj):
        return UserRelationship.objects.filter(follower=obj).count()

    def get_posts(self, obj):
        posts = Post.objects.filter(author=obj)
        return PostSerializer(posts, many=True).data


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.full_name")

    class Meta:
        model = Post
        fields = ("id", "title", "content", "created_at", "author")


class PostListSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source="author.full_name")

    class Meta:
        model = Post
        fields = ("id", "title", "content", "author", "author_name", "created_at")
