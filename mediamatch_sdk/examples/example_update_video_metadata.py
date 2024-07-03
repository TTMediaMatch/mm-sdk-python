from mediamatch_sdk.client import MediaMatchSDKClient

def main():
    # STEP 1: Initialize the SDK
    client_id = "cli_ee1a59258ae8c1601a4c0eb5f2da66b0f63fcb8c5ec91a451ad544b37677be91"
    client_secret = "caa970543a82aaa7eeeadf85f62c57146f6f2c0dfee8f65570e11aaaa3824a91"
    sdk_client = MediaMatchSDKClient(client_id, client_secret)

    # STEP 2: Create a video metadata update job
    asset_metadata = {
        "metadataInfo": {
            "title": "BigBuckBunny",
            "copyrightTerritories": [
                "DZ"
            ],
        }
    }
    asset_id = 7219207559314931717
    try:
        update_response = sdk_client.video_asset_service.update_video_asset_metadata(asset_id, asset_metadata)
        print(update_response)  # if status is SUCCESS means updated metadata successfully
        status = update_response.get('data').get('status')
        if status == 'SUCCESS':
            print("Updated metadata successfully")
    except Exception as e:
        print(f"An error occurred while updating the metadata of this asset: {e}")
        return

    # STEP 3: if the above status is PROCESSING, get batchID, then check the final status by get_delivery_status,
    # this can take up to an hour until it become success
    # batch_id = update_response.get('data').get('batchID')
    # try:
    #     delivery_status = sdk_client.video_upload_service.get_delivery_status(batch_id)
    #     print(delivery_status)
    # except Exception as e:
    #     print(f"An error occurred querying delivery status: {e}")

if __name__ == "__main__":
    main()
