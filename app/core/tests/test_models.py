from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    def test_create_user_with_email(self):
        email = 'abc@gmail.com'
        password = '123123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)

    def test_create_user_email_nomarlized(self):
        email = 'haha@GMAIL.com'
        password = '123123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email.lower())

    def test_create_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '1234')

    def test_create_super_user(self):
        user = get_user_model().objects.create_superuser(
            'admin@gmail.com', '123123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
