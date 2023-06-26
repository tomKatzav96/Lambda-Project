#!/bin/bash


echo "Package the dependencies"
pip install --target ./wikipedia/package wikipedia-api boto3
zip -r ./wikipedia/my-deployment-package.zip ./wikipedia/package/*

zip ./wikipedia/my-deployment-package.zip ./wikipedia/lambda_function.py

echo "Deploy the lambda function"
aws lambda update-function-code --function-name get-info --zip-file fileb://wikipedia/my-deployment-package.zip