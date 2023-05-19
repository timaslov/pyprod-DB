from rest_framework.views import APIView, Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from ....serializers import UserSerializer, UserRegisterSerializer, GiveStaffPermissionsSerializer
from ....services import register_new_user, set_user_permission_level
from ....permissions import IsSuperUser


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


class GiveStaffPermissionsView(APIView):
    permission_classes = [IsSuperUser]
    serializer_class = GiveStaffPermissionsSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = set_user_permission_level(
            serializer.validated_data["email"],
            serializer.validated_data["is_staff"]
        )

        return Response({"success": result})
