#!/bin/bash


echo "Package the dependencies"
pip install --target ./get_info/package wikipedia-api boto3
zip -r ./get_info/my-deployment-package.zip ./get_info/package/*

zip ./get_info/my-deployment-package.zip ./get_info/lambda_function.py

echo "Deploy the lambda function"
aws lambda update-function-code --function-name get-info --zip-file fileb://get_info/my-deployment-package.zip