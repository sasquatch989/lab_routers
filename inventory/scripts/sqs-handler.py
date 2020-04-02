import boto3

# Create SQS client
queue_url = 'https://sqs.us-east-1.amazonaws.com/477286093069/github_webhook_sqs.fifo'
sqs = boto3.resource('sqs', region_name='us-east-1')

q = sqs.Queue(queue_url)

# Receive message from SQS queue
response = q.receive_messages(

    AttributeNames=[
        'All'
    ],
    MaxNumberOfMessages=1,
    MessageAttributeNames=[
        'All'
    ],
    VisibilityTimeout=30,
    WaitTimeSeconds=0
)
print(response)
message = response[0].body
receipt_handle = response[0].receipt_handle

# Delete received message from queue
q.delete_messages(
    Entries=[
        {
            'Id': 'IdString',
            'ReceiptHandle': receipt_handle
        }
    ]
)
print('Received and deleted message: %s' % message)