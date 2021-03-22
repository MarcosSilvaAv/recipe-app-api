from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is succefull"""
        email = 'geral@marcossilva.eu'
        password = '123qwe'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'geral@MARCOSSILVA.EU'

        user = get_user_model().objects.create_user(
            email,
            '123qwe'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test user creted with no email"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '123qwe')

    def test_create_new_superuser(self):
        """Teste creating new super user"""

        user = get_user_model().objects.create_superuser(
            'test@test.com',
            '123qwe'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
