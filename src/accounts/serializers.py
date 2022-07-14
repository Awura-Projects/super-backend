from django.contrib.auth.models import Group
from rest_framework import serializers

from authentication.serializers import UserSerializer
from .models import Employee, Supplier, Delivery

class EmployeeSerializer(serializers.ModelSerializer):
    """
    Employee account create serializer
    """
    id = serializers.HyperlinkedIdentityField('employee-detail')
    user = UserSerializer()
    class Meta:
        """
        Meta class
        """
        model = Employee
        fields = (
            'id',
            'user',
            'profile_picture',
            'birthdate',
            'identification_card',
        )

    def create(self, validated_data):
        user_validated_data = validated_data.pop('user')

        group, created = Group.objects.get_or_create(name='employee')

        user = UserSerializer.create(
            UserSerializer(),
            validated_data=user_validated_data
        )

        user.groups.add(group)
        user.save()

        validated_data['user'] = user

        employee = super().create(validated_data)
        employee.user = user

        return employee

class EmployeeUpdateSerializer(serializers.ModelSerializer):
    """
    Employee account update serializer
    """
    id = serializers.HyperlinkedIdentityField('employee-detail')
    class Meta:
        """
        Meta class
        """
        model = Employee
        fields = (
            'id',
            'profile_picture',
            'birthdate',
            'identification_card',
        )


class SupplierSerializer(serializers.ModelSerializer):
    """
    Supplier account create serializer
    """
    id = serializers.HyperlinkedIdentityField('supplier-detail')
    user = UserSerializer()
    class Meta:
        """
        Meta class
        """
        model = Supplier
        fields = (
            'id',
            'user',
            'profile_picture',
            'birthdate',
            'identification_card',
        )

    def create(self, validated_data):
        user_validated_data = validated_data.pop('user')

        group, created = Group.objects.get_or_create(name='Supplier')

        user = UserSerializer.create(
            UserSerializer(),
            validated_data=user_validated_data
        )

        user.groups.add(group)
        user.save()

        validated_data['user'] = user

        Supplier = super().create(validated_data)
        Supplier.user = user

        return Supplier

class SupplierUpdateSerializer(serializers.ModelSerializer):
    """
    Supplier account update serializer
    """
    id = serializers.HyperlinkedIdentityField('supplier-detail')
    class Meta:
        """
        Meta class
        """
        model = Supplier
        fields = (
            'id',
            'profile_picture',
            'birthdate',
            'identification_card',
        )


class DeliverySerializer(serializers.ModelSerializer):
    """
    Delivery account create serializer
    """
    id = serializers.HyperlinkedIdentityField('delivery-detail')
    user = UserSerializer()
    class Meta:
        """
        Meta class
        """
        model = Delivery
        fields = (
            'id',
            'user',
            'profile_picture',
            'birthdate',
            'identification_card',
        )

    def create(self, validated_data):
        user_validated_data = validated_data.pop('user')

        group, created = Group.objects.get_or_create(name='Delivery')

        user = UserSerializer.create(
            UserSerializer(),
            validated_data=user_validated_data
        )

        user.groups.add(group)
        user.save()

        validated_data['user'] = user

        Delivery = super().create(validated_data)
        Delivery.user = user

        return Delivery

class DeliveryUpdateSerializer(serializers.ModelSerializer):
    """
    Delivery account update serializer
    """
    id = serializers.HyperlinkedIdentityField('delivery-detail')
    class Meta:
        """
        Meta class
        """
        model = Delivery
        fields = (
            'id',
            'profile_picture',
            'birthdate',
            'identification_card',
        )
