from rest_framework import generics, permissions

from api_1_0 import serializers

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = serializers.UserRegistrationSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save()
