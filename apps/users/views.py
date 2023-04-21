from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from apps.users.models import StoreUser
from apps.users.serializers import StoreUserCreateSerializer


class StoreUserCreateAPIView(CreateAPIView):
    queryset = StoreUser.objects.all()
    serializer_class = StoreUserCreateSerializer
    permission_classes = [AllowAny]

