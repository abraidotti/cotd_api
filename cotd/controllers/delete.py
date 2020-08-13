
import boto3
import os

dynamodb = boto3.resource("dynamodb")


def delete(event, context):
    table = dynamodb.Table(os.environ["DYNAMODB_TABLE"])

    try:
        table.delete_item(
            Key={
                "user_id": event["pathParameters"]["user_id"],
                "cotd_id": event["pathParameters"]["cotd_id"],
            }
        )
    except:
        print("Error deleting item.")
        response = {
            "statusCode": 404
        }
        return response

    response = {
        "statusCode": 200
    }

    return response
