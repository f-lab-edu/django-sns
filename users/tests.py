from django.test import TestCase

# Create your tests here.
class UserModelTest(TestCase):
    def test_user_creation(self):
        from users.models import User
        user = User.objects.create_user(
            username="test_username",
            password="test123",
            name="test_name",
            email="test@test.test"
        )
        self.assertEqual(user.username, "test_username")
        self.assertTrue(user.check_password("test123"))
        self.assertEqual(user.name, "test_name")
        self.assertEqual(user.email, "test@test.test")