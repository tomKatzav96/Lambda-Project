import json
import requests


def lambda_handler(event, context):
    # Get the base, target, and the amount from the user
    body = json.loads(event.get('body', '{}'))
    base = body.get('base')  # The base currency
    target = body.get('target')  # The target currency
    amount = body.get('amount')  # The amount to convert

    # Make a request to the exchange rate API and get data
    url = f'https://v6.exchangerate-api.com/v6/13eda48c3e939f9e06d651b2/pair/{base}/{target}/{amount}'
    response = requests.get(url)
    byte_string = response.content

    # Decode the byte string into a regular string using UTF-8 encoding
    regular_string = byte_string.decode('utf-8')

    # Find the start and end index of the conversion result in the string
    start_index = regular_string.find('"conversion_result":') + len('"conversion_result":')
    end_index = regular_string.find(',', start_index)

    # Extract the conversion result from the string
    conversion_result2 = regular_string[start_index:end_index]
    conversion_result = str(conversion_result2)

    # Prepare the response data
    res = {"data": conversion_result}

    return {
        'statusCode': 200,
        'headers': {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": 'GET, POST, PUT, DELETE, OPTIONS'
        },
        'body': json.dumps(res)  # Return the data sent to the backend lambda function as the API response.
    }
