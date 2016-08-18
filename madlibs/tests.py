from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest

from madlibs.views import home_page
from madlibs.models import Field,Madlib
from madlibs.views import match_case

class HomePageTest(TestCase):
	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		self.assertTrue(response.content.startswith(b'<html>'))
		self.assertIn(b'<title>Madlibs viewer</title>',response.content)
		self.assertTrue(response.content.endswith(b'</html>'))

class MadlibModelTest(TestCase):
	def test_new_madlib_exists(self):
		self.assertFalse(Madlib.objects.all().exists())
		#self.assertIn('precipice',Madlib.objects.get(title="An Ass and a Man").text)

class MatchCaseTest(TestCase):
	def test_match_case(self):
		self.assertEqual(match_case('Hello','WORLD'),'World')
		self.assertEqual(match_case('Hello','WORlD'),'World')
		self.assertEqual(match_case('HELLO','world'),'WORLD')
		self.assertEqual(match_case('hello','WORLD'),'world')
		
class 