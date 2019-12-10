import json


def echo(event, context):
    try:
        ip = event['requestContext']['identity']['sourceIp']
    except KeyError as e:
        print(event)
        print(e)
        ip = 'Not found'

    body = {
        "message": "Go Serverless!",
        "caller_ip": ip
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
