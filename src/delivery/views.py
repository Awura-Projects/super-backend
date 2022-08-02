# deliverabel cart list (method)
# cart.object.filter to list all the cart delivery man is null
# serilizer tetkemash cart id becha mekebl
# accept cart id check weather it is valid or not ketyaza teyzual menanin eyalen 
# using cart ide and post method 
# cart.deliveryman = request.user
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import generics
from rest_framework.response import Response

from orders.models import Cart
from orders.serializers import CartSerializer

class DeliveryListAPIView(generics.ListAPIView):
    serializer_class = CartSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.DjangoModelPermissions
    ]

    def get_queryset(self):


        queryset = Cart.objects.filter(payed=True, closed=True, delivery=True)
        return queryset

class DeliveryCloseAPIView(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.DjangoModelPermissions,
    ]

    def get_object(self, pk):
        try:
            return Cart.object.get(pk=pk)
            # return Cart.object.get(pk=pk, delivery=False) other method

        except:
            raise Http404


    def post(self, request, pk, format=None):
        cart = self.get_object(pk)
        if cart.delivery is False:
            return Response({"error": "this delivery has been closed "}, status=400)
        cart.delivery = False
        cart.delivery_man = request.user
        return Response(status=200)
