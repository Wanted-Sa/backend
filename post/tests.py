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


class PostListAPITest(APITestCase):
    @classmethod
    def setUpTestData(self):
        self.user_data = {"email": "test@test.com", "password": "test1234!"}
        self.user = Account.objects.create_user("test@test.com", "test1234!")
        for _ in range(10):
            Post.objects.create(title="test", content="test", account=self.user)
    
    def setUp(self):
        self.access_token = self.client.post(reverse("signin_view"), self.user_data).data["access_token"]
        
    def test_post_list_success(self):
        response = self.client.get(
            path=reverse("post_list_view"),
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
        )
        self.assertEqual(response.status_code, 200)

    def test_post_list_anonymous_fail(self):
        response = self.client.get(
            path=reverse("post_list_view"),
        )
        self.assertEqual(response.status_code, 401)
        
        
class PostDetailAPITest(APITestCase):
    @classmethod
    def setUpTestData(self):
        self.user_data = {"email": "test@test.com", "password": "test1234!"}
        self.user = Account.objects.create_user("test@test.com", "test1234!")
    
    def setUp(self):
        self.access_token = self.client.post(reverse("signin_view"), self.user_data).data["access_token"]
    
    def test_post_detail_success(self):
        post = Post.objects.create(title="test", content="test", account=self.user)
        response = self.client.get(
            path=reverse("post_detail_view", kwargs={"post_id": post.id}),
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
        )
        self.assertEqual(response.status_code, 200)
        
    def test_post_detail_anonymous_fail(self):
        post = Post.objects.create(title="test", content="test", account=self.user)
        response = self.client.get(
            path=reverse("post_detail_view", kwargs={"post_id": post.id}),
        )
        self.assertEqual(response.status_code, 401)
        
    def test_post_detail_not_found_fail(self):
        response = self.client.get(
            path=reverse("post_detail_view", kwargs={"post_id": 1}),
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
        )
        self.assertEqual(response.status_code, 404)
    
    
class PostUpdateAPITest(APITestCase):
    @classmethod
    def setUpTestData(self):
        self.user_data = {"email": "test@test.com", "password": "test1234!"}
        self.anothor_user_data = {"email": "test1@test.com", "password": "test1234!"}
        self.user = Account.objects.create_user("test@test.com", "test1234!")
        self.anothor_user = Account.objects.create_user("test1@test.com", "test1234!")
        self.post_data = {"title": "test1", "content": "test1"}
        self.post = Post.objects.create(title="test", content="test", account=self.user)
        
    def setUp(self):
        self.user_access_token = self.client.post(reverse("signin_view"), self.user_data).data["access_token"]
        self.anothor_user_access_token = self.client.post(reverse("signin_view"), self.anothor_user_data).data["access_token"]
        
    def test_post_update_success(self):
        response = self.client.put(
            path=reverse("post_detail_view", kwargs={"post_id": self.post.id}),
            HTTP_AUTHORIZATION=f"Bearer {self.user_access_token}",
            data=self.post_data,
        )
        self.assertEqual(response.status_code, 200)
    
    def test_post_update_anonymous_fail(self):
        response = self.client.put(
            path=reverse("post_detail_view", kwargs={"post_id": self.post.id}),
            data=self.post_data,
        )
        self.assertEqual(response.status_code, 401)
    
    def test_post_update_not_found_fail(self):
        response = self.client.put(
            path=reverse("post_detail_view", kwargs={"post_id": 10}),
            HTTP_AUTHORIZATION=f"Bearer {self.user_access_token}",
            data=self.post_data,
        )
        self.assertEqual(response.status_code, 404)
        
    def test_post_update_not_owner_fail(self):
        response = self.client.put(
            path=reverse("post_detail_view", kwargs={"post_id": self.post.id}),
            HTTP_AUTHORIZATION=f"Bearer {self.anothor_user_access_token}",
            data=self.post_data,
        )
        self.assertEqual(response.status_code, 403)
        
    def test_post_update_title_not_field_fail(self):
        response = self.client.put(
            path=reverse("post_detail_view", kwargs={"post_id": self.post.id}),
            HTTP_AUTHORIZATION=f"Bearer {self.user_access_token}",
            data={"content": "test"},
        )
        self.assertEqual(response.status_code, 400)
        
    def test_post_update_content_not_field_fail(self):
        response = self.client.put(
            path=reverse("post_detail_view", kwargs={"post_id": self.post.id}),
            HTTP_AUTHORIZATION=f"Bearer {self.user_access_token}",
            data={"title": "test"},
        )
        self.assertEqual(response.status_code, 400)