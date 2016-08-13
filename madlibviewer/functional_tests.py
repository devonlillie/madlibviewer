from selenium import webdriver
import unittest



class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
		
	def tearDown(self):
		self.browser.quit()
		
	# She comes back tomorrow and wants to view her madlibs
	# she clicks into her profile and a link to her madlib is listed under history.
	def test_can_view_old_madlib(self):
		# She comes back tomorrow and wants to view her madlibs
		self.browser.get('http://localhost:8000')
		
		# She looks at the title and sees madlibs in it
		self.assertIn('Madlib',self.browser.title)
		self.fail('Finish the test!')
		
		# She is presented with a form for required inputs and text boxes
		
		# She fills in her answers for each prompt and submits

		# The page refreshes to show her the filled in madlib
	
		# She thinks its hilarious so she saves the madlib to view later if she wants.
		
if __name__=='__main__':
	unittest.main(warnings='ignore')