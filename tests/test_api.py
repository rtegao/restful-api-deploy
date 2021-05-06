import unittest
from flask_app.app import app
import json

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_service(self):
        #arrange
        uri = "/model"

        #body
        body = {
            "sentences":"Absolutely wonderful - silky and sexy and comfortable"
            }

        #act
        response = self.client.post(uri,data=body)

        #assert
        exp_response = {
            "model_prediction": 1
        }

        self.assertEqual(response.json['response']['model_prediction'],exp_response['model_prediction'])

if __name__ == '__main__':
    unittest.main()
    
