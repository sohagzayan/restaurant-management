from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Restaurant

class RestaurantTestCase(APITestCase):
    def test_create_restaurant(self):
        url = reverse('restaurant-list-create')
        data = {'name': 'Test Restaurant'}
        self.client.force_authenticate(user=self.user)  # Assuming you have a user authenticated
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
