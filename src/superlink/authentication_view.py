from rest_framework_simplejwt.views import TokenObtainPairView

from .authentication_serializers import TokenObtainSerializer


class TokenObtainView(TokenObtainPairView):
    serializer_class = TokenObtainSerializer
