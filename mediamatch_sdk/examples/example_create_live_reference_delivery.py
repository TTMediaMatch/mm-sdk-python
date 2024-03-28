from mediamatch_sdk.client import MediaMatchSDKClient

def main():
    # STEP 1: Initialize the SDK
    client_id = "cli_fcf0a39c9d04e22bdccf5c8f7e4b94c271f38aede738d01523ad101643ab8e7e"
    client_secret = "7b310bac07a52c552589d2f9166c9873fadbc186141edac1c2892e63568c5fff"
    sdk_client = MediaMatchSDKClient(client_id, client_secret)

    # STEP 2: Create a delivery job and retrieve the streaming address
    # Metadata about the live reference to be uploaded
    asset_metadata = {
        "assetCategory": "tv",
        "deliveryTitle": "live upload",
        "uploadInfo": {
            "copyrightTerritories": [
                "DZ"
            ],
            "title": "api test - live asset"
        }
    }

    try:
        delivery_response = sdk_client.live_upload_service.create_delivery_job(asset_metadata)
        batch_id = delivery_response.get('data').get('batchID')
        rtmpsURL = delivery_response.get('data').get('streamInfo').get('rtmpsURL')
        print(batch_id)
        print(rtmpsURL)
        if not batch_id:
            raise ValueError("Failed to create delivery job or retrieve job_id")
        print(f"Delivery job created successfully with batch id: {batch_id}, rtmpsURL: {rtmpsURL}")
    except Exception as e:
        print(f"An error occurred while creating the delivery job: {e}")
        return



    #STEP 3: if needed, you can check the delivery address again with the batch_id
    try:
        stream_info = sdk_client.live_upload_service.get_live_delivery_url(batch_id)
        batch_id = stream_info.get('data').get('stream')
        rtmpsURL = stream_info.get('data').get('rtmpsURL')
        print(f"Retrieved streaming url with batch id: {batch_id}, rtmpsURL: {rtmpsURL}")
    except Exception as e:
        print(f"An error occurred querying delivery status: {e}")

if __name__ == "__main__":
    main()
