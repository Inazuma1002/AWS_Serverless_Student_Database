import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('studentDatabase')

def lambda_handler(event, context):
    student_id = event['studentid']
    age = event['age']
    name = event['name']
    student_class = event['class']

    response = table.put_item(
        Item = {
            'studentid' : student_id,
            'age' : age,
            'name' : name,
            'class' : student_class
        }
    )

    return {
        'statusCode' : 200,
        'body' : json.dumps('Student added successfully')
    }

    
