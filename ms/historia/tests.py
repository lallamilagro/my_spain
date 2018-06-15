from django.test import TestCase


class TestHistoriaPage(TestCase):

    def test_page_exists(self):
        response = self.client.get('/historia/')
        self.assertEqual(response.status_code, 200)

    def test_contains_expected_content(self):
        response = self.client.get('/historia/')
        self.assertContains(response, 'Historia de España')
