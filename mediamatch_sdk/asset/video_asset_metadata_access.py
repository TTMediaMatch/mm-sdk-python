import os

from mediamatch_sdk.base_client import BaseClient
from mediamatch_sdk.util.util import extract_error_message


class VideoAssetMetadataAccess(BaseClient):
    def __init__(self, access_token):
        super().__init__(access_token)  # Initialize the BaseClient with the access token

    def get_video_asset_metadata(self, asset_id):
        response = self._get(path=f"/openapi/asset/v1/video/assets/{asset_id}/metadata")
        if response.status_code == 200:
            return response.json()
        else:
            error_msg = extract_error_message(response)
            raise Exception(f"Failed to get the metadata of this video asset.\nError Message: {error_msg}")