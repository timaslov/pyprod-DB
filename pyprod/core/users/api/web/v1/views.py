from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from ....serializers import UserSerializer, UserRegisterSerializer
from ....services import register_new_user


class RegisterUserView(CreateAPIView):
    serializer_class = UserRegisterSerializer

    def perform_create(self, serializer):
        data = serializer.validated_data
        user = register_new_user(
            first_name=data["first_name"],
            last_name=data["last_name"],
            username=data["username"],
            email=data["email"],
            password=data["password"],
        )


class UserView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
