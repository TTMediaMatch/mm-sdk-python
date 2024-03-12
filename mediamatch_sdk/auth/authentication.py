import os

from mediamatch_sdk.base_client import BaseClient


class Authentication(BaseClient):
    def __init__(self, clientID=None, clientSecret=None):
        # If clientID and clientSecret are not provided, read from environment variables
        self.clientID = clientID if clientID is not None else os.getenv('MM_CLIENT_ID')
        self.clientSecret = clientSecret if clientSecret is not None else os.getenv('MM_CLIENT_SECRET')

        if not self.clientID or not self.clientSecret:
            raise ValueError("Client ID and Client Secret must be provided or set as environment variables")
        super().__init__()

    def login(self):
        # todo update
        response = self._post(path="/openapi/token", json={"client_id": self.clientID, "client_secret": self.clientSecret})
        if response.status_code == 200:
            token = response.json().get('data').get("access_token")
            self.session.headers.update({"Authorization": f"Bearer {token}"})
            return token
        else:
            # todo remove
            return 12345
            #raise Exception("Failed to initialize video upload")
