from django.test import TestCase


class TestHomePage(TestCase):

    def test_homepage_exists(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


  
class TestBlogPage(TestCase):

    def test_page_exists(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_contains_expected_content(self):
        response = self.client.get('/blog/')
        self.assertContains(response, 'Hello hello!')

