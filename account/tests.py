from rest_framework.test import APITestCase

from django.urls import reverse

from account.models import Account


class SingupAPITest(APITestCase):
    def test_signup_success(self):
        url = reverse('signup_view')
        user_data = {
            'email': 'test@test.com',
            'password': 'test1234!',
        }
        response = self.client.post(url, user_data)
        self.assertEqual(response.status_code, 201)
        
    def test_signup_email_invalid_fail(self):
        url = reverse('signup_view')
        user_data = {
            'email': 'test.com',
            'password': 'test1234!',
        }
        response = self.client.post(url, user_data)
        self.assertEqual(response.status_code, 400)
        
    def test_signup_password_validation_fail(self):
        url = reverse('signup_view')
        user_data = {
            'email': 'test@test.com',
            'password': 'tes',
        }
        response = self.client.post(url, user_data)
        self.assertEqual(response.status_code, 400)
        
    def test_signup_email_not_field_fail(self):
        url = reverse('signup_view')
        user_data = {
            'password': 'test1234!',
        }
        response = self.client.post(url, user_data)
        self.assertEqual(response.status_code, 400)        
    
    def test_signup_password_not_field_fail(self):
        url = reverse('signup_view')
        user_data = {
            'email': 'test@test.com',
        }
        response = self.client.post(url, user_data)
        self.assertEqual(response.status_code, 400)    
        

class SigninAPITest(APITestCase):
    @classmethod
    def setUpTestData(self):
        self.user_data = {"email": "test@test.com", "password": "test1234!"}
        self.user = Account.objects.create_user("test@test.com", "test1234!")

    def test_signin_success(self):
        url = reverse('signin_view')
        response = self.client.post(url, self.user_data)
        self.assertEqual(response.status_code, 200)
    
    def test_signin_account_not_exist_fail(self):
        url = reverse('signin_view')
        user_data = {
            'email': 'test!test.com',
            'password':'test1234!',
        }
        response = self.client.post(url, user_data)
        self.assertEqual(response.status_code, 400)
        
    def test_signin_email_invalid_fail(self):
        url = reverse('signin_view')
        user_data = {
            'email': 'test.com',
            'password': 'test1234!',
        }
        response = self.client.post(url, user_data)
        self.assertEqual(response.status_code, 400)
        
    def test_signin_password_validation_fail(self):
        url = reverse('signin_view')
        user_data = {
            'email': 'test@test.com',
            'password': 'tes',
        }
        response = self.client.post(url, user_data)
        self.assertEqual(response.status_code, 400)
        
    def test_signin_email_not_field_fail(self):
        url = reverse('signin_view')
        user_data = {
            'password': 'test1234!',
        }
        response = self.client.post(url, user_data)
        self.assertEqual(response.status_code, 400)        
    
    def test_signin_password_not_field_fail(self):
        url = reverse('signin_view')
        user_data = {
            'email': 'test@test.com',
        }
        response = self.client.post(url, user_data)
        self.assertEqual(response.status_code, 400)