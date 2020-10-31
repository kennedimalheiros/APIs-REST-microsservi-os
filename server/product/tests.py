from django.test import TestCase
from rest_framework.test import APITestCase


class ProductAPITest(APITestCase):

    def test_url_api_exist(self):
        response = self.client.get('/product/')
        self.assertEqual(response.status_code, 200)
