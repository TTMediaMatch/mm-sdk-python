import base64
import os

from mediamatch_sdk.base_client import BaseClient
from mediamatch_sdk.util.util import extract_error_message


def _read_image_as_base64(image_path):
    with open(image_path, 'rb') as image_file:
        byte_content = image_file.read()
        base64_content = base64.b64encode(byte_content).decode('utf-8')
        return base64_content


class ImageUpload(BaseClient):
    def __init__(self, access_token):
        super().__init__(access_token)  # Initialize the BaseClient with the access token

    def create_delivery_job(self, metadata):
        """Create an upload delivery job with asset metadata."""
        response = self._post(path="/openapi/upload/v1/image/deliveries", json=metadata)
        print(response.headers)
        if response.status_code == 200:
            return response.json()  # Assuming this returns the batch_id
        else:
            error_msg = extract_error_message(response)
            raise Exception(f"Failed to create delivery job.\nError Message: {error_msg}")

    def get_delivery_status(self, batch_id):
        """Query an upload batch by ID"""
        response = self._get(path=f"/openapi/upload/v1/image/deliveries/{batch_id}")
        if response.status_code == 200:
            return response.json()  # Assuming this returns the batch_id, job_id
        else:
            error_msg = extract_error_message(response)
            raise Exception(f"Failed to query delivery job.\nError Message: {error_msg}")

    def create_delivery_job_with_local_image(self, metadata, image_path):
        """Create an upload delivery job with asset metadata."""
        base64_content = _read_image_as_base64(image_path)
        file_name = os.path.basename(image_path)
        metadata["uploadInfo"]["imageData"] = base64_content
        metadata["uploadInfo"]["referenceFilename"] = file_name
        return self.create_delivery_job(metadata=metadata)
