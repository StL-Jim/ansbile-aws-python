'''
https://boto3.amazonaws.com/v1/documentation/api/latest/guide/sqs.html

How to use Boto3 with an AWS service. In this sample tutorial, you will learn 
how to use Boto3 with Amazon Simple Queue Service (SQS)
'''
from boto3 import resource

# Get the service resource
sqs = resource('sqs', region_name='us-east-2')

# Create the queue. This returns an SQS.Queue instance
queue = sqs.create_queue(QueueName='jimtest', Attributes={'DelaySeconds': '5'})

# You can now access identifiers and attributes
print(queue.url)
print(queue.attributes.get('DelaySeconds'))

# Get the queue. This returns an SQS.Queue instance
getQueue = sqs.get_queue_by_name(QueueName='jimtest')

# Print out each queue name, which is part of its ARN
for queue in sqs.queues.all():
    print(queue.url)

response = queue.send_message(MessageBody='Hello World')

# The response is NOT a resource, but gives you a message ID and MD5
print(response.get('MessageId'))
print(response.get('MD5OfMessageBody'))

# Create messages with custom attributes:
queue.send_message(MessageBody='boto3', MessageAttributes={
    'Author': {
        'StringValue': 'Jim',
        'DataType': 'String'
    }
})

# Messages can also be sent in batches. For example, sending the two messages described above in a single request would look like the following:
response = queue.send_messages(Entries=[
    {
        'Id': '1',
        'MessageBody': 'Hello World 2'
    },
    {
        'Id': '2',
        'MessageBody': 'boto3',
        'MessageAttributes': {
            'Author': {
                'StringValue': 'Jim',
                'DataType': 'String'
            }
        }
    }
])

# Print out any failures
print(response.get('Failed'))

# ---------------------------
# Now get an existing queue
queue = sqs.get_queue_by_name(QueueName='jimtest')

# Process messages by printing out body and optional author name
for message in queue.receive_messages(MessageAttributeNames=['Author']):
    # Get the custom author message attribute if it was set
    author_text = ''
    if message.message_attributes is not None:
        author_name = message.message_attributes.get('Author').get('StringValue')
        if author_name:
            author_text = ' ({0})'.format(author_name)

    # Print out the body and author (if set)
    print('Hello, {0}!{1}'.format(message.body, author_text))
    
    # Let the queue know that the message is processed
    message.delete()

