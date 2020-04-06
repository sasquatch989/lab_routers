#!/usr/bin/env python3

import boto3
import os
from handlers.tower.awxApi import AWX

# Need check if variable set
queue_url = os.environ['SQS_GITHUB_URL']
sqs = boto3.resource('sqs', region_name='us-east-1')

q = sqs.Queue(queue_url)

while True:
    response = q.receive_messages(
        AttributeNames=['SentTimestamp'],
        MaxNumberOfMessages=10,
        VisibilityTimeout=10,
        WaitTimeSeconds=20
    )

    try:
        message = response[0].body
        receipt_handle = response[0].receipt_handle
        q.delete_messages(Entries=[
            {'Id': response[0].attributes['SentTimestamp'], 'ReceiptHandle': receipt_handle}
            ]
        )
        # Insert awx call here
        a = AWX()
        a.get_token()
        a.api_call()

        print('Message received and processed')
    except IndexError:
        print('Index is empty...')