import unittest
from app import create_app

class TestPersonalityChecklistApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the Personality Checklist', response.data)

    def test_results_page(self):
        response = self.client.post('/submit', data={'question1': 'value1', 'question2': 'value2'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Your results are:', response.data)

    def test_invalid_submission(self):
        response = self.client.post('/submit', data={})
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Please answer all questions', response.data)

if __name__ == '__main__':
    unittest.main()