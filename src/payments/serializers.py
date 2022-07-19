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
    customer = serializers.HyperlinkedIdentityField('customer-detail')
    cart = serializers.HyperlinkedIdentityField('cart-detail')
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    payment_date = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Payment
        fields = (
            'customer',
            'cart',
            'total_amount',
            'payment_date',
            'reciept',
        )

    def create(self, validated_data):
        cart = validated_data.get('cart')
        payment = super().create(validated_data)
        cart_items = cart.items.all()
        cart_items_amounts = list(map(cart_item_calculator, cart_items))
        total_amount = sum(cart_items_amounts)
        payment.total_amount = total_amount

        return payment
