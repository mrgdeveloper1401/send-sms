from rest_framework.urls import path
from accounts.views import UserCreateApiView

urlpatterns = [
    path('create_user/', UserCreateApiView.as_view(), name='create_user'),

]