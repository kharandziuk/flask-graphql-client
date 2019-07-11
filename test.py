from unittest import TestCase
from flask_webtest import TestApp
from main import app
import solution

class ExampleTest(TestCase):
    def setUp(self):
        self.app = app
        self.w = TestApp(self.app)

    def test(self):
        r = self.w.post_json('/link', {
            'amount': 313,
            'payment_reference': 'AB1273',
            'payment_date': '2018-01-13'
        })
        self.assertEqual(r.text, '1')

    def test_invalid_output(self):
        r = self.w.post_json('/link', {
            'amount': 313,
            'payment_date': '2018-01-13'
            },
            expect_errors=True
        )
        assert r.status_code == 422
