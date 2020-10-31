import json
import requests
from django.test import TestCase

from rest_framework.test import APITestCase
from unittest.mock import patch

from client.settings import URL_API_SERVER
from .models import Product


class ProductTest(TestCase):
    def setUp(self):
        self.product = Product(barcode=225588, name='Produto Test')

    def test_instance(self):
        self.assertIsInstance(self.product, Product)
        self.assertEqual(self.product.barcode, 225588)
        self.assertEqual(self.product.name, 'Produto Test')

    def test_str(self):
        product = Product(barcode=225588, name='Produto Test')

        self.assertEqual(str(product), f'({self.product.barcode}) - {self.product.name}')


class ProductAPITest(APITestCase):

    def test_url_api_exist(self):
        response = self.client.get('/product/')
        self.assertEqual(response.status_code, 200)

    @patch('product.views.requests.get')
    def test_get_api_product_not_existe(self, mocked_api_product):
        mocked_api_product.return_value.json.return_value = {'barcode': 7891150009585,
                                                             'name': 'Tempero Knorr Meu Assado Limão e Orégano 25g | 15 unidades'
                                                             }
        self.client.get(f'{URL_API_SERVER}product/7891150009585/')
        product = Product.objects.get(pk=7891150009585)
        self.assertEqual(product.barcode, 7891150009585)
        self.assertEqual(product.name, 'Tempero Knorr Meu Assado Limão e Orégano 25g | 15 unidades')

    def test_get_api_product_existe(self):
        product = Product(barcode=7891150009585, name='Tempero Knorr Meu Assado Limão e Orégano 25g | 15 unidades')
        product.save()
        self.client.get(f'/product/7891150009585/')
        product = Product.objects.get(pk=7891150009585)
        self.assertEqual(product.barcode, 7891150009585)
        self.assertEqual(product.name, 'Tempero Knorr Meu Assado Limão e Orégano 25g | 15 unidades')

    @patch('product.views.requests.get')
    def test_get_error(self, mocked_api_product):
        mocked_api_product.side_effect = requests.exceptions.ConnectionError
        with self.assertRaises(requests.exceptions.ConnectionError):
            requests.get(f'{URL_API_SERVER}product/{999999}')

    @patch('product.views.requests.get')
    def test_get_error_response(self, mocked_api_product):
        mocked_api_product.side_effect = requests.exceptions.ConnectionError
        response = self.client.get(f'/product/999999999999/')
        self.assertEqual(response.json(), f'Erro interno do servidor, Produto 999999999999 não encontrado.')

    @patch('product.views.requests.get')
    def test_get_server_error_response(self, mocked_api_product):
        mocked_api_product.return_value.json.return_value = {'Error': 'Não encontrado'}
        response = self.client.get(f'/product/999999999999/')
        self.assertEqual(response.json(), 'Produto 999999999999 não encontrado.')

