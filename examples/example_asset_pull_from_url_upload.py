from mediamatch_sdk.client import MediaMatchSDKClient

def main():
    # STEP 1: Initialize the SDK
    client_id = "cli_fcf0a39c9d04e22bdccf5c8f7e4b94c271f38aede738d01523ad101643ab8e7e"
    client_secret = "7a0388a17b3e75139fda645be6f052467a4781a71b6c22a006415803a050ffc9"
    sdk_client = MediaMatchSDKClient(client_id, client_secret)

    # STEP 2: Create a delivery job
    # Metadata about the video reference to be uploaded
    asset_metadata = {
        "uploadType": "PULL_FROM_URL",
        "assetCategory": "tv",
        "deliveryTitle": "api test 1 pull from google",
        "uploadInfo": {
            "copyrightTerritories": [
                "DZ"
            ],
            "referenceFilename": "BigBuckBunny.mp4",
            "duration": 22,
            "title": "BigBuckBunny",
            "videoURL": "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"
            #"videoURL": "https://bytedance-s3-va-mediamatch-upload.s3.amazonaws.com/ogc-tvod-us-east-1/sjq_test_05/a.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIATOBZI4K7CFLAIWUP/20240319/us-east-1/s3/aws4_request&X-Amz-Date=20240319T231552Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=83a0f54f7e97361224171eaf155c494d2e8d1e0b6f3ef7d845418c261c5e9753"
        }
    }

    try:
        delivery_response = sdk_client.video_upload_service.create_delivery_job(asset_metadata)
        batch_id = delivery_response.get('data').get('batchID')
        if not batch_id:
            raise ValueError("Failed to create delivery job or retrieve batch_id")
        print(f"Delivery job created successfully with batch id: {batch_id}")
    except Exception as e:
        print(f"An error occurred while creating the delivery job: {e}")
        return

    # STEP 3: Check the delivery status, this can take up to an hour until it become success
    # try:
    #     delivery_status = sdk_client.video_upload_service.get_delivery_status(batch_id)
    #     print(delivery_status)
    # except Exception as e:
    #     print(f"An error occurred querying delivery status: {e}")

if __name__ == "__main__":
    main()
