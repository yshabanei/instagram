from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from activity.models import Comment, Like

User = get_user_model()


class CommentCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = ("caption", "post", "reply_to", "user")
        extra_kwargs = {"reply_to": {"required": False}}

    @staticmethod
    def validate_caption(attr):
        if len(attr) > 30:
            raise ValidationError(_("Caption cannot be more than 30 characters"))
        return attr

    @staticmethod
    def validate_reply_to(attr):
        if attr.reply_to is not None:
            raise ValidationError(_("You can not reply to a reply recursively"))
        return attr

    def validate(self, attrs):
        return attrs


class CommentRepliesListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username")

    class Meta:
        model = Comment
        fields = ("id", "caption", "user", "reply_to")


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ("post",)
        

class LikeSerializer(serializers.ModelSerializer):
    user =serializers.CharField(source='user.username')
    class Meta:
        model = Like
        fields = ("user",)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class CommentListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    replies_count = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ("id", "caption", "user", "replies_count")

    @staticmethod
    def get_replies_count(obj):
        qs = obj.replies_count.all()
        if qs.count() > 10:
            qs = qs[:10]

        serializer = CommentRepliesListSerializer(qs, many=True)
        return serializer.data
