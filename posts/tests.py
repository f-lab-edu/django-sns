from django.test import TestCase

from posts.models import Post
from users.models import User
# Create your tests here.
class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username = "test",
            password = "test123",
            name = "tester",
            email = "test@test.test"
        )

    def test_post_creation(self):
        post = Post.objects.create(
            user = self.user,
            content = "test post",
            image = "",
        )

        self.assertEqual(post.user.username, "test")
        self.assertEqual(post.content, "test post")
        self.assertTrue(hasattr(post, "created_at"))
        self.assertTrue(hasattr(post, "updated_at"))