from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets # if we use viewsets, it will do crud operation by itself 
from rest_framework.response import Response
# from rest_framework import permissions





class ProductViewSet(viewsets.ModelViewSet):   
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]
    # permission_classes = (permissions.IsAuthenticatedOrIsAdmin)

    def list(self, request):
        producer = request.GET.get('producer')
        product_name = request.GET.get('product_name')
        queryset = self.filter_queryset(self.get_queryset())


        if producer is not None:
            queryset = queryset.filter(producer__title__icontains=producer)
        if product_name is not None:
            queryset = queryset.filter(products=product_name)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

   

 