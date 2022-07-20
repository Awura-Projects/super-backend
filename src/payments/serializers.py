from django.conf import settings
from rest_framework import serializers

from orders.models import CartItem
from .models import Payment

def cart_item_calculator(cart_item :CartItem):
    quantity = cart_item.quantity
    unit_price = cart_item.unit_price
    discount = cart_item.discount
    discounted_price = unit_price - (unit_price * discount)

    return quantity * discounted_price


class PaymentSerailzer(serializers.ModelSerializer):
    user = serializers.HyperlinkedIdentityField('customer-detail')
    cart = serializers.HyperlinkedIdentityField('cart-detail')
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    payment_date = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Payment
        fields = (
            'user',
            'cart',
            'card_number',
            'card_holder',
            'total_amount',
            'payment_date',
        )

    def validate_card_number(self, value):
        if not value in settings.VALID_CARD_NUMBERS:
            raise serializers.ValidationError(
                'Invalid card number'
            )
        return value

    def validate_cart(self, value):
        cart = value
        request = self.context.get('request')
        user = request.user
        if cart.user != user:
            raise serializers.ValidationError(
                "This cart is not yours."
            )
        if not cart.closed:
            raise serializers.ValidationError(
                "Cart is not closed."
            )

        return value

    def create(self, validated_data):
        cart = validated_data.get('cart')
        payment = super().create(validated_data)
        cart_items = cart.items.all()
        cart_items_amounts = list(map(cart_item_calculator, cart_items))
        total_amount = sum(cart_items_amounts)
        payment.total_amount = total_amount

        return payment
