from django.test import TestCase


class TestHistoryPage(TestCase):

    def test_page_exists(self):
        response = self.client.get('/history/')
        self.assertEqual(response.status_code, 200)

    def test_contains_expected_content(self):
        response = self.client.get('/history/')
        self.assertContains(response, 'Historia de España')
