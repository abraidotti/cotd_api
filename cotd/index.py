from .controllers.create import create
from .controllers.delete import delete
from .controllers.get import get
from .controllers.get_all import get_all
from .controllers.update import update


def handler(event, context):
    print("event in index.handler:", event)

    if(event["httpMethod"] == "GET"):
        if(event["resource"] == "/user/{user_id}/cotd/{cotd_id}"):
            return get(event, context)
        # get all
        if (event["resource"] == "/user/{user_id}/cotd"):
            return get_all(event, context)

    # create one
    if (event["httpMethod"] == "POST"):
        if (event["resource"] == "/user/{user_id}/cotd"):
            return create(event, context)

    # update one
    if (event["httpMethod"] == "PUT"):
        if (event["resource"] == "/user/{user_id}/cotd/{cotd_id}"):
            return update(event, context)

    # delete one
    if (event["httpMethod"] == "DELETE"):
        if (event["resource"] == "/user/{user_id}/cotd/{cotd_id}"):
            return delete(event, context)

    return {
        "statusCode": 404
    }
