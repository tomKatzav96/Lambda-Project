import unittest
import json
import sys
sys.path.append(".")
from money_api.lambda_function import lambda_handler

class UnitTestCurrencyConverte(unittest.TestCase):
    
    def test_correct_input(self):
        event = {
            'body': '{"base": "USD", "target": "ILS", "amount": 100}'
        }
        expected_result = {
            'statusCode': 200,
            'headers': {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": 'GET, POST, PUT, DELETE, OPTIONS'
            },
            'body': '{"data": "372.88"}'
        }

        result = lambda_handler(event, None)
        body_data = json.loads(result['body'])
        expected_data = float(body_data['data'])

        self.assertLessEqual(370, expected_data)
        self.assertGreaterEqual(375, expected_data)

if __name__ == '__main__':
    unittest.main()
