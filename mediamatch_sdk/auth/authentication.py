import os

from mediamatch_sdk.base_client import BaseClient
from requests.auth import HTTPBasicAuth
import base64


class Authentication(BaseClient):
    def __init__(self, clientID=None, clientSecret=None):
        # If clientID and clientSecret are not provided, read from environment variables
        self.clientID = clientID if clientID is not None else os.getenv('MM_CLIENT_ID')
        self.clientSecret = clientSecret if clientSecret is not None else os.getenv('MM_CLIENT_SECRET')

        if not self.clientID or not self.clientSecret:
            raise ValueError("Client ID and Client Secret must be provided or set as environment variables")
        super().__init__()

    def login(self):
        grantType = {
            'grantType': 'client_credential'
        }

        credentials = f"{self.clientID}:{self.clientSecret}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()
        print(encoded_credentials)
        self.session.headers.update({"Authorization": f"Basic {encoded_credentials}"})
        response = self._post(path="/openapi/auth/v1/token", json=grantType)
        if response.status_code == 200:
            token = response.json().get('data').get("access_token")
            self.session.headers.update({"Authorization": f"Bearer {token}"})
            return token
        else:
            raise Exception("Failed to authenticate")
