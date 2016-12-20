from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            User.USERNAME_FIELD,
            User._meta.pk.name,
            'password',
        )

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
