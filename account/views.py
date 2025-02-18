from .models import User
from rest_framework.viewsets import GenericViewSet,ModelViewSet
from rest_framework.response import Response
from .permission import IsAuthenticatedAndOwnerUser
from .serializers import UserSerializer

class UserMnagement(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedAndOwnerUser]


