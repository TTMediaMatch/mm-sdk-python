import os

from mediamatch_sdk.base_client import BaseClient
from mediamatch_sdk.util.util import extract_error_message


class VideoAssetMetadataUpdate(BaseClient):
    def __init__(self, access_token):
        super().__init__(access_token)  # Initialize the BaseClient with the access token

    def update_video_asset_metadata(self, asset_id, metadata):
        response = self._put(path=f"/openapi/asset/v1/video/assets/{asset_id}", json=metadata)
        if response.status_code == 200:
            return response.json()
        else:
            error_msg = extract_error_message(response)
            raise Exception(f"Failed to update the metadata of this video asset.\nError Message: {error_msg}")