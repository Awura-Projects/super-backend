from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from model_utils import Choices

from .models import User

class UserSerializer(serializers.ModelSerializer):
    """
    A serializer for the user model
    """
    # id = serializers.HyperlinkedIdentityField('user-detail')
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    confirm_password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    user_type = serializers.CharField(read_only=True)
    class Meta:
        """
        Meta class
        """
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'password',
            'confirm_password',
            'phone',
            'user_type',
        )

    def validate_password(self, value):
        validate_password(value)
        return value
    
    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError(
                {
                    'password': 'Passwords doesn\'t match',
                }
            )

        return attrs
    
    def create(self, validated_data):
        validated_data.pop("confirm_password")

        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)

        return user

class PasswordChangeForm(serializers.Serializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    new_password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    confirm_password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    def validate_password(self, value):
        request = self.context.get('request')
        user = request.user

        if not user.check_password(value):
            raise serializers.ValidationError(
                {
                    'password': 'The entered password is not valid',
                }
            )

        return value

    def validate_new_password(self, value):
        validate_password(value)

        return value

    def validate(self, attrs):
        new_password = attrs.get('new_password')
        confirm_password = attrs.get('confirm_password')

        if new_password != confirm_password:
            raise serializers.ValidationError(
                {
                    'new_password': 'Passwords don\'t match',
                }
            )

        return attrs

    def save(self):
        request = self.context.get('request')
        user = request.user

        password = self.validated_data['new_password']
        user.set_password(password)
        user.save()
