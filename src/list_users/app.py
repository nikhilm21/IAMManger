import boto3
import os
import json


def lambda_handler(message, context):

    table_name = os.environ.get('TABLE', 'Activities')
    region = os.environ.get('REGION', 'us-east-1')
    aws_environment = os.environ.get('AWSENV', 'AWS')

    activities_table = boto3.resource( 'dynamodb',region_name=region)

    table = activities_table.Table(table_name)

    response = table.scan()
    print(response['Items'])

    return {
            'statusCode': 400,
            'headers': {},
            'body': json.dumps(response['Items'])
            }
        