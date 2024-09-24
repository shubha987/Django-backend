from django.test import SimpleTestCase
from django.urls import reverse, resolve
from irisApp.views import predictor

class TestUrls(SimpleTestCase):
    def test_predictor_url_resolves(self):
        url = reverse('predictor')
        self.assertEqual(resolve(url).func, predictor)
