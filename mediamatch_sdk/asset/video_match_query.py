import os

from mediamatch_sdk.base_client import BaseClient
from mediamatch_sdk.util.util import extract_error_message


class VideoMatchQuery(BaseClient):
    def __init__(self, access_token):
        super().__init__(access_token)  # Initialize the BaseClient with the access token

    def get_video_match(self, asset_id,start_time,end_time,page=None,pageSize=None):
        if (page == None or pageSize == None):
            response = self._get(path=f"openapi/asset/v1/video/assets/{asset_id}/matchinfo?startTime={start_time}&endTime={end_time}")
        else:
            response = self._get(path=f"openapi/asset/v1/video/assets/{asset_id}/matchinfo?startTime={start_time}&endTime={end_time}&page={page}&pageSize={pageSize}")
        if response.status_code == 200:
            return response.json()  # Assuming this returns the stream_info
        else:
            error_msg = extract_error_message(response)
            raise Exception(f"Failed to get live delivery url.\nError Message: {error_msg}")