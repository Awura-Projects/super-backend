from rest_framework import serializers

from products.models import Product
from .models import Cart, CartItem

class CartItemSerializer(serializers.ModelSerializer):
    # product = serializers.HyperlinkedIdentityField('product-detail')
    unit_price = serializers.DecimalField(max_digits=6, decimal_places=2, read_only=True)
    discount = serializers.DecimalField(max_digits=6, decimal_places=2, read_only=True)
    class Meta:
        model = CartItem
        fields = (
            'product',
            'quantity',
            'unit_price',
            'discount',
        )

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                {
                    'quantity': 'This field should be a positive integer'
                }
            )

        return value

    def validate(self, attrs):
        product = attrs.get('product')
        quantity = attrs.get('quantity')
        if product.amount < quantity:
            raise serializers.ValidationError(
                {
                    'quantity': 'The quantity is larger than the available amount'
                }
            )

        return attrs

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user

        product = validated_data['product']
        quantity = validated_data['quantity']

        cart_set = user.cart_set.filter(closed=False)
        if cart_set.exists():
            cart = cart_set.first()
        else:
            cart = Cart.objects.create(
                user=user,
            )

        cart_item = cart.items.filter(product=product)
        if cart_item.exists():
            cart_item = cart_item.first()
            old_quantity = cart_item.quantity
            cart_item.quantity = old_quantity + quantity

        else:
            cart_item = CartItem.objects.create(
                cart=cart,
                product=product,
                quantity=quantity,
                unit_price=product.price,
                discount=product.discount
            )

        product.amount = product.amount - cart_item.quantity
        product.save()

        return cart_item

    def update(self, instance, validated_data):
        product = validated_data['product']
        old_quantity = instance.quantity
        new_quantity = product.amount + old_quantity - cart_item.quantity

        if new_quantity < 0:
            raise serializers.ValidationError(
                {
                    'quantity': 'The quantity is larger than tha available amount'
                }
            )
        cart_item = super().update(instance, validated_data)
        product.amount = new_quantity
        product.save()

        return cart_item

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
