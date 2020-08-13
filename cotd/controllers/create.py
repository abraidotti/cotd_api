import datetime
import json
import logging
import os
import random
import boto3
import uuid

dynamodb = boto3.resource("dynamodb")


def create(event, context):
    timestamp = datetime.datetime.now().replace(microsecond=0).isoformat()

    table = dynamodb.Table(os.environ["DYNAMODB_TABLE"])

    cards = ("2C", "2D", "2H", "2S",
             "3C", "3D", "3H", "3S",
             "4C", "4D", "4H", "4S",
             "5C", "5D", "5H", "5S",
             "6C", "6D", "6H", "6S",
             "7C", "7D", "7H", "7S",
             "8C", "8D", "8H", "8S",
             "9C", "9D", "9H", "9S",
             "10C", "10D", "10H", "10S",
             "JC", "JD", "JH", "JS",
             "QC", "QD", "QH", "QS",
             "KC", "KD", "KH", "KS",
             "AC", "AD", "AH", "AS")

    item = {
        "user_id": event["pathParameters"]["user_id"],
        "cotd_id": str(uuid.uuid1()),
        "card": random.choice(cards),
        "createdAt": timestamp,
        "updatedAt": timestamp,
    }

    table.put_item(Item=item)

    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return response
