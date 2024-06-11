"""danielcaz_lambda_utils.responses

This module contain the class to build responses to be returned by the API Gateway.
"""

from json import dumps as json_dumps


class ApiGatewayResponse:
    """ Class to build responses to be returned by the API Gateway. """

    def __init__(self, methods: list[str], origins: list[str]):
        """Initializes the class with the methods and origins allowed.

        Args:
            methods (list[str]): List of HTTP methods allowed.
            origins (list[str]): List of origins allowed.

        Returns:
            None
        """
        self.methods = methods
        self.origins = origins

    def build_response(self, status_code: int, body: dict) -> dict:
        """Builds the response to be returned by the API Gateway.

        Args:
            status_code (int): HTTP status code.
            body (dict): Body of the response.

        Returns:
            dict: Response to be returned by the API Gateway.
        """
        return {
            'headers': {
                'Access-Control-Allow-Methods': ', '.join(self.methods),
                'Access-Control-Allow-Origin': ', '.join(self.origins),
            },
            'statusCode': status_code,
            'body': json_dumps(body),
        }
