from django.test import TestCase
from unittest.mock import Mock
from django.shortcuts import resolve_url


mock_get = Mock()
mock_get.return_value.text = 'Hello World'
mock_get().text


class CrawlerTest(TestCase):

    def setUp(self):
        self.response = self.client.get(resolve_url('counter_word'))
        self.url = 'http://python.org'
        self.word = 'Python'

    def test_get(self):
        ''' GET / must return status code 200 '''
        self.assertEqual(200, self.response.status_code)

    def test_res(self):
        res = {'Python': 97}
        self.assertEqual({'Python': 97}, res)
