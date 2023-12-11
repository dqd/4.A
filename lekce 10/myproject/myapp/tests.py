from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class ViewTestCase(TestCase):
    def test_display_index(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_display_registration(self):
        response = self.client.get(reverse("registration"))
        self.assertEqual(response.status_code, 200)

    def test_register_user(self):
        username = "john_smith"
        password = "abcdabcd"

        self.assertFalse(User.objects.filter(username=username).exists())

        response = self.client.post(
            reverse("registration"),
            {
                "username": username,
                "password1": password,
                "password2": password,
            },
        )

        self.assertIsNotNone(User.objects.filter(username=username).first())
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("login"))
