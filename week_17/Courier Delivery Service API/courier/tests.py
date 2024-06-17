from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from django.test import TestCase
from .models import CustomUser

class CustomUserTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(username='testuser', password='testpassword', role='admin')
        self.token = RefreshToken.for_user(self.user)

    def test_get_users_unauth(self):
        response = self.client.get(reverse('users'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_users_auth(self):
        self.client.credentials(HTTP_AUTHORIZATION = f'Bearer {self.token.access_token}')
        response = self.client.get(reverse('users'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_custom_user(self):
        response = self.client.post(reverse('users'), {'username': 'test_admin', 'password': 'test_password', 'role': 'admin'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
