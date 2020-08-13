import datetime
import json
import logging
import os

import boto3

dynamodb = boto3.resource("dynamodb")


def update(event, context):
    data = json.loads(event["body"])
    if "text" not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't update the item.")

    timestamp = datetime.datetime.now().replace(microsecond=0).isoformat()

    table = dynamodb.Table(os.environ["DYNAMODB_TABLE"])

    result = table.update_item(
        Key={
            "user_id": event["pathParameters"]["user_id"],
            "cotd_id": event["pathParameters"]["cotd_id"],
        },
        ExpressionAttributeNames={
            "#cotd_text": "text",
        },
        ExpressionAttributeValues={
            ":text": data["text"],
            ":updatedAt": timestamp,
        },
        UpdateExpression="SET #cotd_text = :text, "
                         "updatedAt = :updatedAt",
        ReturnValues="ALL_NEW",
    )

    response = {
        "statusCode": 200,
        "body": json.dumps(result["Attributes"])
    }

    return response
