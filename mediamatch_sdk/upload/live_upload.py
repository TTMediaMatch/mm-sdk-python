import os

from mediamatch_sdk.base_client import BaseClient
from mediamatch_sdk.util.util import extract_error_message


class LiveUpload(BaseClient):
    def __init__(self, access_token):
        super().__init__(access_token)  # Initialize the BaseClient with the access token

    def create_delivery_job(self, metadata):
        response = self._post(path="/openapi/upload/v1/live/deliveries", json=metadata)
        if response.status_code == 200:
            return response.json()  # Assuming this returns the batch_id, stream_info
        else:
            error_msg = extract_error_message(response)
            raise Exception(f"Failed to create live delivery job.\nError Message: {error_msg}")

    def get_live_delivery_url(self, batch_id):
        response = self._get(path=f"/openapi/upload/v1/live/deliveries/{batch_id}/streamPushInfo")
        if response.status_code == 200:
            return response.json()  # Assuming this returns the stream_info
        else:
            error_msg = extract_error_message(response)
            raise Exception(f"Failed to get live delivery url.\nError Message: {error_msg}")

    def get_delivery_status(self, batch_id):
        response = self._get(path=f"/openapi/upload/v1/live/deliveries/{batch_id}")
        # 打印请求信息
        print("Request URL:", response.request.url)
        print("Request Method:", response.request.method)
        print("Request Headers:", response.request.headers)
        print("Request Body:", response.request.body)

        # 打印响应信息
        print("\nResponse Status Code:", response.status_code)
        print("Response Headers:", response.headers)
        print("Response Content:", response.text)
        if response.status_code == 200:
            return response.json()  # Assuming this returns the stream_info
        else:
            error_msg = extract_error_message(response)
            raise Exception(f"Failed to get live delivery url.\nError Message: {error_msg}")
