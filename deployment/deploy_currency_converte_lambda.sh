#!/bin/bash

echo "Package the dependencies"
pip install --target ./money_api/package requests
zip -r ./money_api/my-deployment-package.zip ./money_api/package/*

zip ./money_api/my-deployment-package.zip ./money_api/lambda_function.py

echo "Deploy the lambda function"
aws lambda update-function-code --function-name Currency_Converter --zip-file fileb://money_api/my-deployment-package.zip
