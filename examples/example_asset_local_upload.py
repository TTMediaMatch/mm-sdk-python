from mediamatch_sdk.client import MediaMatchSDKClient

def main():

    # Initialize the SDK

    # if you have set environment variables (MM_CLIENT_ID, MM_CLIENT_SECRET)
    # sdk_client = MediaMatchSDKClient()

    # or pass in them explicitly
    client_id = "sampleid"
    client_secret = "samplesecrete"
    sdk_client = MediaMatchSDKClient(client_id, client_secret)

    # STEP 1: Create a delivery job
    # Metadata about the video reference to be uploaded
    asset_metadata = {
        "uploadType": "FILE_UPLOAD",
        "assetCategory": "tv",
        "deliveryTitle": "api test 1",
        "uploadInfo": {
            "copyrightTerritories": [
                "DZ"
            ],
            "referenceFilename": "IMG_1234.MOV",
            "duration": 22,
            "title": "api test movie"
        }
    }

    # STEP 2: Upload the actual video file
    try:
        # delivery_response = sdk_client.video_upload_service.create_delivery_job(asset_metadata)
        # batch_id = delivery_response.get('batch_id')
        batch_id = 123345
        if not batch_id:
            raise ValueError("Failed to create delivery job or retrieve job_id")
        print(f"Delivery job created successfully with job_id: {batch_id}")
    except Exception as e:
        print(f"An error occurred while creating the delivery job: {e}")
        return

    #filepath = "/Users/bytedance/Downloads/test_northern_light.MOV"
    filepath = "/Users/bytedance/Downloads/IMG_9794.MOV"
    #filepath = "/Users/bytedance/Downloads/IMG_6331.MP4"

    # Proceed with the video upload
    try:
        upload_response = sdk_client.video_upload_service.upload_video(filepath, batch_id, 5*1024**2)
        print(upload_response)
    except Exception as e:
        print(f"An error occurred during the video upload: {e}")


if __name__ == "__main__":
    main()
