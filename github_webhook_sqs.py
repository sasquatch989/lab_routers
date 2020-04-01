import json
import boto3
from time import ctime


def lambda_handler(event, context):
    d = boto3.resource('dynamodb')
    dT = d.Table('github_webhook_sqs')
    #dt.put_item(Item={'MessageId':str(event)})
    dT.put_item(Item={'event_date': ctime(), 'data': event})

    s = boto3.resource('sqs')
    q = s.Queue('https://sqs.us-east-1.amazonaws.com/477286093069/github_webhook_sqs.fifo')
    q.send_message(MessageBody=str(event), MessageGroupId="github_webhook_sqs")

    return {
        'statusCode': 200,
        'body': event
    }