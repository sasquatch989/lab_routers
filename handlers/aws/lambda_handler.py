import json
import boto3
import os
from time import ctime


def lambda_handler(event, context):
    d = boto3.resource('dynamodb')
    dt = d.Table('github_webhook_sqs')
    dt.put_item(Item={'event_date': ctime(), 'data': 'Github push received'})

    # Using env variable for sqs_url
    s = boto3.resource('sqs')
    sq = s.Queue(os.environ['sqs_url'])
    sq.send_message(MessageBody='Github push received')

    return {
        'statusCode': 200,
        'body': 'Webhook done'
    }