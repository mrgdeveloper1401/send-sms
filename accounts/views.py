from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView

from accounts.models import User
from accounts.serializers import UserCreateSerializer, RequestOtpSerializer


class UserCreateApiView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()


class RequestOtpApiView(APIView):
    def post(self, request):
        ser_data = RequestOtpSerializer(data=request.data)
        if ser_data.is_valid():
            pass
        else:
            pass