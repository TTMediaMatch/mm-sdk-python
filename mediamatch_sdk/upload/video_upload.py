import os
import time

from mediamatch_sdk.base_client import BaseClient
from mediamatch_sdk.util.util import extract_error_message


class VideoUpload(BaseClient):
    def __init__(self, access_token):
        super().__init__(access_token)  # Initialize the BaseClient with the access token

    def create_delivery_job(self, metadata):
        """Create an upload delivery job with asset metadata."""
        response = self._post(path="/openapi/upload/v1/video/deliveries", json=metadata)
        if response.status_code == 200:
            return response.json()  # Assuming this returns the batch_id
        else:
            error_msg = extract_error_message(response)
            raise Exception(f"Failed to create delivery job.\nError Message: {error_msg}")

    def get_delivery_status(self, batch_id):
        """Query an upload batch by ID"""
        response = self._get(path=f"openapi/upload/v1/video/deliveries/{batch_id}")
        if response.status_code == 200:
            return response.json()  # Assuming this returns the batch_id, job_id
        else:
            error_msg = extract_error_message(response)
            raise Exception(f"Failed to query delivery job.\nError Message: {error_msg}")

    def initialize_upload(self, file_path, batch_id, file_size, chunk_size, chunk_count):
        file_name = os.path.basename(file_path)
        print(f"The file name is: {file_name}")
        file_meta = {
            'fileName': file_name,
            'batchID': str(batch_id),
            'sourceInfo': {
                'videoSize': file_size,
                'chunkSize': chunk_size,
                'totalChunkCount': chunk_count
            }
        }
        print(f"Prepare Video Upload Metadata: {file_meta}")
        print(self.base_url)
        response = self._post(path="/openapi/upload/v1/video/uploads/init", json=file_meta)
        if response.status_code == 200:
            return response.json()
        else:
            error_msg = extract_error_message(response)
            raise Exception(f"Failed to initialize video upload.\nError Message: {error_msg}")

    def upload_chunk(self, upload_id, chunk_data, chunk_start, chunk_end, total_size, max_retries=3):
        """Uploads a chunk of the video file with retry logic."""
        self.session.headers.update({
            "Content-Range": f"bytes {chunk_start}-{chunk_end}/{total_size}",
            "Content-Length": str(chunk_end - chunk_start + 1),
            "Content-Type": "video",
        })

        for attempt in range(max_retries):
            response = self._put(path=f"/openapi/upload/v1/video/uploads/{upload_id}/chunk", data=chunk_data)
            if response.status_code in [200, 201, 206]:  # 201 completed, 206 partial uploaded
                return response.json()
            else:
                error_msg = extract_error_message(response)
                print(f"Chunk Upload Failed, status code {response.status_code}, Error Message: {error_msg}, Retry {attempt + 1} of {max_retries}")
        raise Exception("Failed to upload chunk after max retries.")

    # default chunk size 5MB
    def upload_video(self, filepath, batch_id, chunk_size=5242880):
        if chunk_size > 62 * 1024 ** 2:
            raise Exception("Chunk size should not exceed 64MB")

        file_size = os.path.getsize(filepath)

        if file_size < 5 * 1024 ** 2:  # Less than 5 MB
            chunk_size = file_size  # Upload as a whole
        else:
            chunk_size = min(file_size, chunk_size)  # Respect the default or specified chunk size

        chunk_count = calculate_number_of_chunks(file_size, chunk_size)

        response_data = self.initialize_upload(filepath, batch_id, file_size, chunk_size, chunk_count)
        upload_id = response_data.get('data').get('uploadID')

        with open(filepath, 'rb') as f:
            total_size = file_size

            chunk_start = 0
            chunk_index = 0
            while chunk_start < file_size and chunk_index < chunk_count:
                f.seek(chunk_start)

                # Last chunk
                if chunk_index == chunk_count - 1:
                    last_chunk_size = file_size - chunk_start
                    chunk_data = f.read(last_chunk_size)
                else:
                    chunk_data = f.read(chunk_size)

                chunk_end = chunk_start + len(chunk_data) - 1
                self.upload_chunk(upload_id, chunk_data, chunk_start, chunk_end, total_size)
                chunk_start += chunk_size
                chunk_index += 1
        return {"message": "Upload complete", "upload_id": upload_id}


def calculate_number_of_chunks(file_size, chunk_size):
    """
    Calculate the number of chunks for a given file size, considering the rules for chunk sizes.

    Args:
    - file_size (int): The size of the file in bytes.
    - chunk_size (int): The size of each chunk in bytes. Default is 5 MB.

    Returns:
    - int: The number of chunks.
    """
    min_chunk_size = 5 * 1024 ** 2  # Minimum chunk size (5 MB)

    # Calculate the number of chunks without considering the final chunk size rule
    full_chunks = file_size // chunk_size
    remaining_size = file_size % chunk_size

    # If there's no remaining size, return the number of full chunks
    if remaining_size == 0:
        return full_chunks

    # If the remaining size is less than or equal to the min size(5mb), merge to the previous chunk
    if remaining_size <= min_chunk_size:
        return full_chunks

    return full_chunks + 1  # Include the last chunk
