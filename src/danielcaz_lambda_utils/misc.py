import json


def build_response(status_code: int, methods: list[str], origins: list[str], body: dict):
    return {
        'headers': {
            'Access-Control-Allow-Methods': ', '.join(methods),
            'Access-Control-Allow-Origin': ', '.join(origins),
        },
        'statusCode': status_code,
        'body': json.dumps(body),
    }
