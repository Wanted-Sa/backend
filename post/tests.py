from rest_framework.test import APITestCase

from django.urls import reverse

from account.models import Account
from post.models import Post

class PostCreateAPITest(APITestCase):
    @classmethod
    def setUpTestData(self):
        self.user_data = {"email": "test@test.com", "password": "test1234!"}
        self.post_data = {"title": "test", "content": "test"}
        self.user = Account.objects.create_user("test@test.com", "test1234!")
    
    def setUp(self):
        self.access_token = self.client.post(reverse("signin_view"), self.user_data).data["access_token"]

    def test_post_create_success(self):
        response = self.client.post(
            path=reverse("post_list_view"),
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
            data=self.post_data,
        )
        self.assertEqual(response.status_code, 201)
        
    def test_post_create_anonymous_fail(self):
        response = self.client.post(
            path=reverse("post_list_view"),
            data=self.post_data,
        )
        self.assertEqual(response.status_code, 401)
    
    def test_post_create_title_not_field_fail(self):
        response = self.client.post(
            path=reverse("post_list_view"),
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
            data={"content": "test"},
        )
        self.assertEqual(response.status_code, 400)
        
    def test_post_create_content_not_field_fail(self):
        response = self.client.post(
            path=reverse("post_list_view"),
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
            data={"title": "test"},
        )
        self.assertEqual(response.status_code, 400)
