from selenium import webdriver
import unittest

class NewTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_generally(self):
        self.browser.get('http://localhost:8000')
        set.assertIn('Project Match', self.browser.title)
        self.fail('Finish the app')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
