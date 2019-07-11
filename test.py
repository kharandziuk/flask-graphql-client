from unittest import TestCase
from flask_webtest import TestApp
from main import app

class ExampleTest(TestCase):
    def setUp(self):
        self.app = app
        self.w = TestApp(self.app)

    def test(self):
        r = self.w.post('/link')
        self.assertEqual(r.text, '1')
