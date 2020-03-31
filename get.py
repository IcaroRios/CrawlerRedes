import boto3
# Get the service resource.
dynamodb = boto3.resource('dynamodb')
client = boto3.client('dynamodb')
table = dynamodb.Table('teste')

response = client.list_global_tables(
    RegionName='us-east-2',
    Limit=100
)

print (response)
