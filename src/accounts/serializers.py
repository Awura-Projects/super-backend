from django.contrib.auth.models import Group
from rest_framework import serializers

from authentication.serializers import UserSeirailzer
from .models import Employee, Supplier, Delivery

class EmployeeCreateSerializer(serializers.ModelSerializer):
    """
    Employee account create serializer
    """
    # id = serializers.HyperlinkedIdentityField('employee-detail')
    user = UserSeirailzer()
    class Meta:
        """
        Meta class
        """
        model = Employee
        fields = (
            'user',
            'profile_picture',
            'birthdate',
            'identification_card',
        )

    def create(self, validated_data):
        user_validated_data = validated_data.pop('user')

        group, created = Group.objects.get_or_create(name='employee')

        user = UserSeralizer.create(
            UserSeirailzer(),
            validated_data=user_validated_data
        )

        user.groups.add(group)
        user.save()

        employee = super().create(validated_data)
        employee.user = user

        return employee

class EmployeeUpdateSerializer(serializers.ModelSerializer):
    """
    Employee account update serializer
    """
    # id = serializers.HyperlinkedIdentityField('employee-detail')
    class Meta:
        """
        Meta class
        """
        model = Employee
        fields = (
            'profile_picture',
            'birthdate',
            'identification_card',
        )
