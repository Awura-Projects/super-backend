from django.conf import settings
from rest_framework import serializers

from orders.models import CartItem, Cart
from .models import Payment


def cart_item_calculator(cart_item: CartItem):
    quantity = cart_item.quantity
    unit_price = cart_item.unit_price
    if cart_item.discount is None:
        discount = 0
    else:
        discount = cart_item.discount
    discounted_price = unit_price - (unit_price * discount)

    return quantity * discounted_price


class CartHyperlinkedRelatedField(serializers.HyperlinkedRelatedField):
    def get_queryset(self):
        request = self.context.get('request')
        user = request.user

        return Cart.objects.filter(user=user)


class CartInputField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        request = self.context.get('request')
        user = request.user

        return Cart.objects.filter(user=user)


class PaymentSerailzer(serializers.ModelSerializer):
    id = serializers.HyperlinkedIdentityField('payment-detail')
    user = serializers.HyperlinkedRelatedField(
        'account-detail', read_only=True)
    cart = CartHyperlinkedRelatedField('cart-detail')
    total_amount = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True)
    payment_date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Payment
        fields = (
            'id',
            'user',
            'cart',
            'card_number',
            'card_holder',
            'total_amount',
            'payment_date',
        )

    def to_internal_value(self, data):
        self.fields['cart'] = CartInputField()
        return super().to_internal_value(data)

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
        payment_queryset = Payment.objects.filter(cart=cart)
        if payment_queryset.exists():
            raise serializers.ValidationError(
                "This cart has already been payed."
            )
        if cart.user != user:
            raise serializers.ValidationError(
                "This cart is not yours."
            )
        if not cart.closed:
            raise serializers.ValidationError(
                'Cart is not closed.'
            )

        return value

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        cart = validated_data.get('cart')
        cart_items = cart.items.all()
        cart_items_amounts = list(map(cart_item_calculator, cart_items))
        total_amount = sum(cart_items_amounts)

        validated_data['total_amount'] = total_amount
        validated_data['user'] = user
        payment = super().create(validated_data)
        cart.payed = True
        cart.save()

        return payment
