from django.test import TestCase

from .. import views


class TestCustomer(TestCase):
    def test_login(self):
        response = self.client.post('/account/login/', {'username': 'admin', 'password': 'admin'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.resolver_match.func, views.user_login)