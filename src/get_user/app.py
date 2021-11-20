import boto3
import os
import json
from boto3.dynamodb.conditions import Key


def lambda_handler(message, context):

    if ('pathParameters' not in message or
            message['httpMethod'] != 'GET'):
        return {
            'statusCode': 400,
            'headers': {},
            'body': json.dumps({'msg': 'Bad Request'})
        }

    table_name = os.environ.get('TABLE', 'Activities')
    region = os.environ.get('REGION', 'us-east-1')
    aws_environment = os.environ.get('AWSENV', 'AWS')

    if aws_environment == 'AWS_SAM_LOCAL':
        activities_table = boto3.resource(
            'dynamodb',
            endpoint_url='http://dynamodb:8000'
        )
    else:
        activities_table = boto3.resource(
            'dynamodb',
            region_name=region
        )

    table = activities_table.Table(table_name)
    activity_id = message['pathParameters']['UserName']
    activity_id = str(activity_id.replace('%7B','').replace('%7D',''))
    print(activity_id)

    
    try:
        response = table.get_item(
            Key = {
                'UserName': activity_id
            }
        )

        return {
        'statusCode': 400,
        'headers': {},
        'body': json.dumps(response['Item'])
        }

    except:
        return {
        'statusCode': 400,
        'headers': {},
        'body': json.dumps({'msg': 'User Not Found'})
        }
