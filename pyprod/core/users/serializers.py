from rest_framework import serializers

from ..models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "is_staff",
            "is_superuser",
        )
        read_only_fields = (
            "id",
            "is_staff",
            "is_superuser",
        )


class UserRegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(allow_blank=False, max_length=25)
    last_name = serializers.CharField(allow_blank=False, max_length=25)
    username = serializers.CharField(allow_blank=False, max_length=25)
    email = serializers.EmailField(allow_blank=False, max_length=255)
    password = serializers.CharField(allow_blank=False, min_length=5)


class GiveStaffPermissionsSerializer(serializers.Serializer):
    email = serializers.EmailField(allow_blank=False, max_length=255)
    is_staff = serializers.BooleanField()
