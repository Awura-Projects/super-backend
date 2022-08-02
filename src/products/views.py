from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets # if we use viewsets, it will do crud operation by itself 


class ProductViewSet(viewsets.ModelViewSet):   
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    # permission_classes = [IsAuthenticated]
