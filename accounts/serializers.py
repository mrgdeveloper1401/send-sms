from rest_framework import serializers

from accounts.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'mobile_phone',
            'password'
        )
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class RequestOtpSerializer(serializers.Serializer):
    mobile_phone = serializers.CharField(required=True)
