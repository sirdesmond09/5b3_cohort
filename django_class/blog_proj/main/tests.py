from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
# Create your tests here.


class TestPostModel(TestCase):
    
    def test_create_model(self):
        user = User.objects.create(username="testuser", password="testpassword123", email="test@gmail.com")
        new_post = Post.objects.create(title="Test title", slug="test-slug", body="this is a test body", author=user)
        all_post = Post.objects.all()
        
        self.assertEqual(new_post.title, "Test title")
        self.assertEqual(new_post.body, "this is a test body")
        self.assertEqual(new_post.author.id, user.id)
        self.assertEqual(all_post.count(), 1)
        self.assertIsInstance(new_post, Post)