import boto3

queue_url = 'https://sqs.us-east-1.amazonaws.com/477286093069/github_webhook_sqs'
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
        q.delete_messages(
            Entries=[
                {
                    'Id': response[0].attributes['SentTimestamp'],
                    'ReceiptHandle': receipt_handle
                }
            ]
        )
        print('Message received and processed')
    except IndexError:
        print('Index is empty...')