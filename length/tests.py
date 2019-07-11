from django.test import TestCase, Client
from django.urls import reverse
import random
random.uniform(1, 100000000000)


class TestLengthConversion(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("length:convert")

    def test_centimetre_to_metre_conversion(self):
        """
        Tests conversion of centimetre measurements tcento metre.
        """
        data = {
            "input_unit": "centimetre",
            "output_unit": "metre",
            "input_value": round(8096.894, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 80.969)

    def test_centimetre_to_mile_conversion(self):
        data = {
            "input_unit": "centimetre",
            "output_unit": "mile",
            "input_value": round(985805791.3527409, 3)
        }
        response = self.client.get(self.url, data)
        self.assertContains(response, 6125.511)