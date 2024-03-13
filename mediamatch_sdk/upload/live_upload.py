import os

from mediamatch_sdk.base_client import BaseClient

class LiveUpload(BaseClient):
    def __init__(self, access_token):
        super().__init__(access_token)  # Initialize the BaseClient with the access token

    def create_delivery_job(self, metadata):
        response = self._post(path="/openapi/upload/v1/live/deliveries/create", json=metadata)
        if response.status_code == 200:
            return response.json()  # Assuming this returns the batch_id, stream_info
        else:
            raise Exception("Failed to create live delivery job")
        
    def get_live_delivery_url(self, batch_id):
        response = self._get(path=f"/openapi/upload/v1/live/deliveries/{batch_id}/streamPushInfo")
        if response.status_code == 200:
            return response.json()  # Assuming this returns the stream_info
        else:
            raise Exception("Failed to get live delivery url")