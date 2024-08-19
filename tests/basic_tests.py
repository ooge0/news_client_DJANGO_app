# Create your tests here.
import os
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from django.test import TestCase
from dotenv import load_dotenv

os.environ['DJANGO_SETTINGS_MODULE'] = 'news.settings'


class ProductListTest(TestCase):
    load_dotenv()

    BASE_DIR = Path(__file__).resolve().parent.parent
    url = os.getenv('BASE_URL')

    def test_home_page_availability(self):
        response = requests.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_home_page_is_html(self):
        response = requests.get(self.url)
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        self.assertTrue(soup.html is not None, "HTML content should have an <html> tag")
        self.assertEqual(response.status_code, 200)

    def test_home_page_header_is_ok(self):
        response = requests.get(f'{self.url}/source/1')
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        # Extract the title from the HTML
        page_title = soup.title.string.strip()

        # Assertions
        self.assertEqual(page_title, 'Source "bbc.com"')
        self.assertEqual(response.status_code, 200)

    def test_check_header_links(self):
        response = requests.get(self.url)
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

        urls = []
        for a_tag in soup.find_all('a', href=True):
            urls.append(a_tag['href'])

        # Here you can perform assertions based on the URLs collected
        self.assertTrue(len(urls) > 0)  # Example: Ensure at least one link is found
