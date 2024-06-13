import os

from mediamatch_sdk.base_client import BaseClient
from mediamatch_sdk.util.util import extract_error_message


class LiveAssetActivate(BaseClient):
    def __init__(self, access_token):
        super().__init__(access_token)  # Initialize the BaseClient with the access token

    def activate_live_asset(self, asset_id):
        response = self._post(path=f"/openapi/asset/v1/live/assets/{asset_id}/activate")
        if response.status_code == 200:
            return response.json()
        else:
            error_msg = extract_error_message(response)
            raise Exception(f"Failed to activate the live asset.\nError Message: {error_msg}")
