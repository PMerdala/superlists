#-*- coding: utf8 -*-
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):
	def test_root_utl_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func,home_page)
		
	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		#sprawdzenie czy szablon jest choć trochę zgodny z założeniem
		#gdybym zrezygnował z tego sprawdzenia mógłbym w szablon wpisać cokolwiek
		self.assertTrue(response.content.startswith(b'<html>'))
		self.assertIn(b'<title>Listy rzeczy do zrobienia</title>',response.content)
		self.assertTrue(response.content.strip().endswith(b'</html>'))
		#sprawdzenie czy wynik pobrania strony jest zgodny z szablonem
		expected_html = render_to_string('home.html')
		self.assertEqual(response.content.decode(),expected_html)
