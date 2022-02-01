from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .. import views


class TestUrls(SimpleTestCase):
    def test_home_page(self):
        url = reverse('shop_home-page')
        self.assertEqual(resolve(url).func, views.home_page)

    def test_product(self):
        url = reverse('product', args=['url'])
        self.assertEqual(resolve(url).func, views.detail_view)
