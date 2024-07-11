
import json
import boto3
from onix_schema.model import ONIXMessage, Product
from utils import send_email, publish_sns, transform_onix_to_csv

s3_client = boto3.client('s3')
ses_client = boto3.client('ses')
sns_client = boto3.client('sns')

def lambda_handler(event, context):
    for record in event['Records']:
        s3_bucket = record['s3']['bucket']['name']
        s3_object_key = record['s3']['object']['key']

        response = s3_client.get_object(Bucket=s3_bucket, Key=s3_object_key)
        content = response['Body'].read().decode('utf-8')

        # Assuming the content is in ONIX XML format, convert it to JSON (pseudo-code)
        onix_message = ONIXMessage.parse_raw(content)  # Replace with actual parsing logic

        # Transform ONIX data to CSV format
        csv_content = transform_onix_to_csv(onix_message)

        # Send the transformed CSV via email
        send_email(ses_client, 'from@example.com', 'to@example.com', 'Subject', 'Body', csv_content, 'output.csv')

        # Publish a notification to SNS
        publish_sns(sns_client, 'SNS_TOPIC_ARN', 'Subject', 'Message')

    return {
        'statusCode': 200,
        'body': json.dumps('Processing complete')
    }
