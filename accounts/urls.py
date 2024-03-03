from rest_framework.urls import path
from accounts.views import UserCreateApiView, RequestOtpApiView

urlpatterns = [
    path('create_user/', UserCreateApiView.as_view(), name='create_user'),
    path('request_user_otp/', RequestOtpApiView.as_view(), name='request_user')

]