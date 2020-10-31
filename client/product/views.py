import requests

from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ProductSerializer

from .models import Product
from client.settings import URL_API_SERVER


class ProductView(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def retrieve(self, request, pk=None):
        if Product.objects.filter(pk=pk).exists():
            product = Product.objects.get(pk=pk)
        else:
            try:
                api_product = requests.get(f'{URL_API_SERVER}product/{pk}').json()
            except requests.exceptions.ConnectionError:
                return Response(f'Erro interno do servidor, Produto {pk} não encontrado.')

            if api_product.get('barcode'):
                product = Product(barcode=api_product.get('barcode'), name=api_product.get('name'))
                product.save()
            else:
                return Response(f'Produto {pk} não encontrado.')

        serializer = ProductSerializer(product)
        return Response(serializer.data)
