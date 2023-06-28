import wikipediaapi
import boto3
import json

def lambda_handler(event, context):
    wiki_wiki = wikipediaapi.Wikipedia('en')  # Creating an instance of the Wikipedia class for English Wikipedia

    # Retrieving the 'topic' parameter from the 'queryStringParameters' dictionary in the 'event' object
    # The 'event' object likely contains information about the triggering event
    page_py = wiki_wiki.page(event['queryStringParameters']['topic'])

    if page_py.exists():  # Checking if the requested Wikipedia page exists
        Title = "%s" % page_py.title  # Extracting the page title
        Top = "%s" % page_py.summary  # Extracting the page summary
        if "may refer to:" in Top:
            return {'statusCode': 400}
        
        file_name = f"{Title}.txt"  # Creating a file name based on the page title with a .txt extension

        client = boto3.client('s3')  # Creating an S3 client using boto3

        # Uploading the page summary to an S3 bucket with the specified file name
        client.put_object(Body=Top, Bucket='tom-katzav-bucket-aws-part-2', Key=file_name)

        return {
            'statusCode': 200,  # Returning a success status code
            'body': Top  # Returning the page summary as the response body
        }
    else:
        return {'statusCode': 400}  # Returning an error status code if the requested Wikipedia page does not exist
    