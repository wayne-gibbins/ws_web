from app import app

import unittest
import json

class CitiesTestCase(unittest.TestCase):

  def test_index(self):
    tester = app.test_client(self)
    response = tester.get('/', content_type='text/html')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.data, "<html>\n<h1>page views</h1>\n\n<h2>1</h2>\n</html>")
if __name__ == '__main__':
    unittest.main()
