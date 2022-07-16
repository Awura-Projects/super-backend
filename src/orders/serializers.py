from rest_framework import serializers

from .models import Cart, CartItem

class CartItemSerializer(serializers.ModelSerializer):
    # product = serializers.HyperlinkedIdentityField('product-detail')
    class Meta:
        model = CartItem
        fields = (
            'product',
            'quantity',
            'unit_price',
            'discount',
        )

class CartSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedIdentityField("customer-detail")
    delivery_man = serializers.HyperlinkedIdentityField("delivery-detail")
    items = CartItemSerializer(many=True)
    class Meta:
        model = Cart
        fields = (
            'user',
            'order_date',
            'delivery_man',
            'closed',
            'closed_time',
            'items',
        )
