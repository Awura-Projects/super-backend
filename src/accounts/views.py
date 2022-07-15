from rest_framework import views
from rest_framework.response import Response

from authentication.serializers import UserSerializer
from .permissions import IsCustomer
from .serializers import CustomerSignupForm, CustomerUpdateForm

class CustomerSignupAPIView(views.APIView):
    serializer_class = CustomerSignupForm

    def post(self, request, format=None):
        serializer = CustomerSignupForm(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        user_serializer = UserSerializer(instance=user)

        return Response(user_serializer.data)


class CustomerUpdateAPIView(views.APIView):
    serializer_class = CustomerUpdateForm
    permission_classes = [IsCustomer]

    def get(self, request):
        user = request.user
        serializer = CustomerUpdateForm(instance=user)

        return Response(serializer.data)

    def put(self, request, pk=None):
        user = request.user
        serializer = CustomerUpdateForm(instance=user, data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data)
