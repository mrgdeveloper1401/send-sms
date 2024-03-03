from rest_framework.generics import CreateAPIView

from accounts.models import User
from accounts.serializers import UserCreateSerializer


class UserCreateApiView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()