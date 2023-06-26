import unittest
import sys
sys.path.append("./wikipedia")
import lambda_function

class UnitTestGetInfo(unittest.TestCase):

    def test_page_exists(self):
        response = lambda_function.lambda_handler({"queryStringParameters": {"topic": 'Python_(programming_language)'}}, "context")
        status = f'{response["statusCode"]}'
        content = f'{response["body"]}'
        expect_status = "200"
        expect_content = "Python is a high-level, general-purpose programming language."
        self.assertEqual(expect_status, status)
        self.assertIn(expect_content, content)

    def test_duplicated_page(self):
        response = lambda_function.lambda_handler({"queryStringParameters": {"topic": 'base'}}, "context")
        status = f'{response["statusCode"]}'
        expect = "400"
        self.assertEqual(expect, status)

    def test_page_missing(self):
        response = lambda_function.lambda_handler({"queryStringParameters": {"topic": 'NonExistingPageWithStrangeName'}}, "context")
        status = f'{response["statusCode"]}'
        expect = "400"
        self.assertEqual(expect, status)

if __name__ == '__main__':
    unittest.main()
