import os

from mediamatch_sdk.base_client import BaseClient
from mediamatch_sdk.util.util import extract_error_message


class LiveAsset(BaseClient):
    def __init__(self, access_token):
        super().__init__(access_token)  # Initialize the BaseClient with the access token

    def update_live_asset_metadata(self, asset_id, metadata):
        response = self._put(path=f"/openapi/asset/v1/live/assets/{asset_id}", json=metadata)
        if response.status_code == 200:
            return response.json()
        else:
            error_msg = extract_error_message(response)
            raise Exception(f"Failed to update the metadata of this live asset.\nError Message: {error_msg}")

    def get_live_asset_metadata(self, asset_id):
        response = self._get(path=f"/openapi/asset/v1/live/assets/{asset_id}/metadata")
        if response.status_code == 200:
            return response.json()
        else:
            error_msg = extract_error_message(response)
            raise Exception(f"Failed to get the metadata of this live asset.\nError Message: {error_msg}")

    def get_live_asset_other_info(self, asset_id):
        response = self._get(path=f"/openapi/asset/v1/live/assets/{asset_id}/information")
        if response.status_code == 200:
            return response.json()
        else:
            error_msg = extract_error_message(response)
            raise Exception(f"Failed to get other information of this live asset.\nError Message: {error_msg}")

    def activate_live_asset(self, asset_id):
        response = self._post(path=f"/openapi/asset/v1/live/assets/{asset_id}/activate")
        if response.status_code == 200:
            return response.json()
        else:
            error_msg = extract_error_message(response)
            raise Exception(f"Failed to activate the live asset.\nError Message: {error_msg}")

    def deactivate_live_asset(self, asset_id):
        response = self._post(path=f"/openapi/asset/v1/live/assets/{asset_id}/deactivate")
        if response.status_code == 200:
            return response.json()
        else:
            error_msg = extract_error_message(response)
            raise Exception(f"Failed to deactivate the live asset.\nError Message: {error_msg}")

    def get_live_match(self, asset_id,start_time,end_time,page = None,pageSize = None):
        if (page == None or pageSize == None):
            response = self._get(path=f"openapi/asset/v1/live/assets/{asset_id}/matchinfo?startTime={start_time}&endTime={end_time}")
        else:
            response = self._get(path=f"openapi/asset/v1/live/assets/{asset_id}/matchinfo?startTime={start_time}&endTime={end_time}&page={page}&pageSize={pageSize}")
        if response.status_code == 200:
            return response.json()  # Assuming this returns the stream_info
        else:
            error_msg = extract_error_message(response)
            raise Exception(f"Failed to get live delivery url.\nError Message: {error_msg}")