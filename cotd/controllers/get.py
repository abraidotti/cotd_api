import boto3
import os
import json

dynamodb = boto3.resource("dynamodb")


def get(event, context):
    table = dynamodb.Table(os.environ["DYNAMODB_TABLE"])

    result = table.get_item(
        Key={
            "user_id": event["pathParameters"]["user_id"],
            "cotd_id": event["pathParameters"]["cotd_id"],
        }
    )

    print(result)

    response = {
        "statusCode": 200,
        "body": json.dumps(result["Item"])
    }

    return response
