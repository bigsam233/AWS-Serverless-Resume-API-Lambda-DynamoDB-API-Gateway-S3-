import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CloudResumeTable')

def lambda_handler(event, context):
    # Update views
    table.update_item(
        Key={'ID': '1'},
        UpdateExpression='ADD #v :inc',
        ExpressionAttributeNames={'#v': 'Views'},
        ExpressionAttributeValues={':inc': 1}
    )

    # Get data
    resume_data = table.get_item(Key={'ID': '1'})

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(resume_data['Item'], default=int)
    }