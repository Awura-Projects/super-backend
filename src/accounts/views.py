from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import EmailMessage
from rest_framework import views, generics, permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse

from authentication.serializers import (
    UserSerializer, PasswordChangeForm,
    PasswordResetForm, ChangePasswordForm
)
from .permissions import (
    IsSelfCustomer,
    IsAdminOrDeliveryOrSelfCustomer,
)
from .serializers import CustomerSignupForm, CustomerUpdateForm

User = get_user_model()
token_generator = PasswordResetTokenGenerator()


class ForgotPasswordAPIView(views.APIView):
    serializer_class = PasswordResetForm

    def post(self, request):
        email = request.data.get('email')
        user = User.objects.filter(email=email)
        if user.exists():
            user = user.first()
            token = token_generator.make_token(user)
            link = reverse('reset-password',
                           kwargs={'uid': user.id, 'token': token}, request=request)
            mail_subject = 'Reset your password'
            message = (f"Hello, {user.get_full_name()}" +
                       "\n\nThere was a request to reset your password." +
                       "If you are the one who requested this service click on the link below." +
                       "If not you can ignore this email. \n\n\n Thank you for your time" +
                       f"Link:- {link}")
            email_message = EmailMessage(mail_subject, message, to=[email])
            email_message.send()

        return Response(
            {
                "data": "If there is a user with email we have sent a reset email. Check your email"
            }, status=200
        )


class PasswordResetAPIView(views.APIView):
    serializer_class = ChangePasswordForm

    def post(self, request, uid=None, token=None):
        user = User.objects.filter(id=uid)
        if user.exists():
            user = user.first()
            if token_generator.check_token(user, token):
                serializer = self.serializer_class(data=request.data)
                serializer.is_valid(raise_exception=True)
                password = serializer.validated_data.get('new_password')
                user.set_password(password)
                user.save()

                return Response(
                    {
                        'data': 'Password changed successfuly'
                    }, status=200
                )

        return Response(
            {
                'data': 'Activation link invalid.'
            }, status=400
        )


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get_object(self):
        user = self.request.user

        return user


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
    permission_classes = [IsSelfCustomer]

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


class PasswordChangeAPIView(views.APIView):
    serializer_class = PasswordChangeForm
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        serializer = PasswordChangeForm(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data)


class AccountRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsAdminOrDeliveryOrSelfCustomer,
    ]
    queryset = User.objects.all()
