from mediamatch_sdk.client import MediaMatchSDKClient

def main():
    # STEP 1: Initialize the SDK
    client_id = "sampleid"
    client_secret = "samplesecrete"
    sdk_client = MediaMatchSDKClient(client_id, client_secret)

    # STEP 2: Create a delivery job
    # Metadata about the video reference to be uploaded
    asset_metadata = {
        "uploadType": "FILE_UPLOAD",
        "assetCategory": "tv",
        "deliveryTitle": "upload from local file",
        "uploadInfo": {
            "copyrightTerritories": [
                "DZ"
            ],
            #"referenceFilename": "IMG_9794.MOV",
            "referenceFilename": "IMG_1234.MOV",
            #"referenceFilename": "test_northern_light.MOV",
            "duration": 22,
            "title": "api test movie"
        }
    }


    try:
        delivery_response = sdk_client.video_upload_service.create_delivery_job(asset_metadata)
        batch_id = delivery_response.get('data').get('batchID')
        print(batch_id)
        if not batch_id:
            raise ValueError("Failed to create delivery job or retrieve job_id")
        print(f"Delivery job created successfully with batch id: {batch_id}")
    except Exception as e:
        print(f"An error occurred while creating the delivery job: {e}")
        return

    # STEP 3: Upload the actual video file
    #filepath = "/Users/bytedance/Downloads/IMG_9794.MOV"
    filepath = "/Users/bytedance/Downloads/IMG_1234.MOV"
    #filepath = "/Users/bytedance/Downloads/IMG_6331.MP4"

    # Proceed with the video upload
    try:
        upload_response = sdk_client.video_upload_service.upload_video(filepath, batch_id, 5*1024**2)
        print(upload_response)
    except Exception as e:
        print(f"An error occurred during the video upload: {e}")

    # STEP 4: Check the delivery status, this can take up to an hour until it become success
    # try:
    #     delivery_status = sdk_client.video_upload_service.get_delivery_status(batch_id)
    #     print(delivery_status)
    # except Exception as e:
    #     print(f"An error occurred querying delivery status: {e}")

if __name__ == "__main__":
    main()
