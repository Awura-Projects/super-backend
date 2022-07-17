from rest_framework import serializers

from products.models import Product
from .models import Cart, CartItem

class CartItemSerializer(serializers.ModelSerializer):
    id = serializers.HyperlinkedIdentityField('cartitem-detail')
    # product = serializers.HyperlinkedIdentityField('product-detail')
    unit_price = serializers.DecimalField(max_digits=6, decimal_places=2, read_only=True)
    discount = serializers.DecimalField(max_digits=6, decimal_places=2, read_only=True)
    class Meta:
        model = CartItem
        fields = (
            'id',
            'product',
            'quantity',
            'unit_price',
            'discount',
        )

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                'This field should be a positive integer greater than 0'
            )

        return value

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user

        product = validated_data['product']
        quantity = validated_data['quantity']
        if product.amount < quantity:
            raise serializers.ValidationError(
                {
                    'quantity': 'The quantity is larger than the available amount'
                }
            )

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
            new_amount = product.amount - quantity
            if new_amount < 0:
                raise serializers.ValidationError(
                    {
                        'quantity': 'The quantity is larger than the available amount'
                    }
                )

            cart_item.quantity = old_quantity + quantity
            cart_item.save()
            product.amount = new_amount
            product.save()

        else:
            cart_item = CartItem.objects.create(
                cart=cart,
                product=product,
                quantity=quantity,
                unit_price=product.price,
                discount=product.discount
            )

            new_amount = product.amount - quantity
            product.amount = new_amount
            product.save()

        return cart_item

    def update(self, instance, validated_data):
        product = validated_data['product']
        quantity = validated_data['quantity']
        old_quantity = instance.quantity
        new_amount = product.amount + old_quantity - quantity

        if new_amount < 0:
            raise serializers.ValidationError(
                {
                    'quantity': 'The quantity is larger than the available amount'
                }
            )
        cart_item = super().update(instance, validated_data)
        product.amount = new_amount
        product.save()

        return cart_item

class CartSerializer(serializers.ModelSerializer):
    id = serializers.HyperlinkedIdentityField('cart-detail')
    user = serializers.HyperlinkedIdentityField("customer-detail")
    delivery_man = serializers.HyperlinkedIdentityField("delivery-detail")
    items = CartItemSerializer(many=True)
    closed = serializers.BooleanField(read_only=True)
    payed = serializers.BooleanField(read_only=True)
    closed_time = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Cart
        fields = (
            'id',
            'user',
            'order_date',
            'delivery_man',
            'closed',
            'payed',
            'closed_time',
            'items',
        )
