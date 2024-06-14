from mediamatch_sdk.client import MediaMatchSDKClient

def main():
    # STEP 1: Initialize the SDK
    client_id = "cli_ee1a59258ae8c1601a4c0eb5f2da66b0f63fcb8c5ec91a451ad544b37677be91"
    client_secret = "caa970543a82aaa7eeeadf85f62c57146f6f2c0dfee8f65570e11aaaa3824a91"
    sdk_client = MediaMatchSDKClient(client_id, client_secret)

    # STEP 2: Create a delivery job
    # Metadata about the video reference to be uploaded
    asset_metadata = {
        "uploadType": "PULL_FROM_URL",
        "assetCategory": "tv",
        "deliveryTitle": "upload by pull from url - test",
        "uploadInfo": {
            "copyrightTerritories": [
                "DZ"
            ],
            "referenceFilename": "BigBuckBunny.mp4",
            "title": "BigBuckBunny",
            "videoURL": "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"
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
    try:
        delivery_status = sdk_client.video_upload_service.get_delivery_status(batch_id)
        print(delivery_status)
    except Exception as e:
        print(f"An error occurred querying delivery status: {e}")

if __name__ == "__main__":
    main()
