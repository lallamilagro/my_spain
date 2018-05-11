from django.test import TestCase


class TestArticlesPage(TestCase):

    def test_page_exists(self):
        response = self.client.get('/articles/')
        self.assertEqual(response.status_code, 200)

    def test_contains_expected_content(self):
        response = self.client.get('/articles/')
        self.assertContains(response, 'Articles')
