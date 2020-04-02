import boto3
from time import ctime

url = ''


def lambda_handler(event, context):
    d = boto3.resource('dynamodb')
    dT = d.Table('github_webhook_sqs')
    dT.put_item(Item={'event_date': ctime(), 'data': 'event received'})

    s = boto3.resource('sqs')
    q = s.Queue(url)
    q.send_message(MessageBody='Push Received', MessageGroupId="github_webhook_sqs")

    return {
        'statusCode': 200,
        'body': 'Webhook done'
    }