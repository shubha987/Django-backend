from django.test import TestCase, Client
from django.urls import reverse  # Import reverse to generate URLs

class PredictorViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_predictor_view(self):
        # Generate the URL using reverse
        url = reverse('predictor')
        
        # Send a POST request with sample data
        response = self.client.post(url, {
            'sepal_length': '5.1',
            'sepal_width': '3.5',
            'petal_length': '1.4',
            'petal_width': '0.2',
        })

        # Check if the response is OK
        self.assertEqual(response.status_code, 200)

        # Check if the predicted result is Setosa
        self.assertContains(response, 'Setosa')

