import boto3
from boto3.dynamodb.conditions import Key
import json
import os


dynamodb = boto3.resource("dynamodb")


def get_all(event, context):
    table = dynamodb.Table(os.environ["DYNAMODB_TABLE"])

    result = table.query(
        KeyConditionExpression=Key("user_id").eq(
            event["pathParameters"]["user_id"])
    )

    print(result)

    response = {
        "statusCode": 200,
        "body": json.dumps(result["Items"])
    }

    return response
