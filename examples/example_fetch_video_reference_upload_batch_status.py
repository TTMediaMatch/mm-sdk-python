import time

from mediamatch_sdk.client import MediaMatchSDKClient

def main():
    # STEP 1: Initialize the SDK
    client_id = "cli_fcf0a39c9d04e22bdccf5c8f7e4b94c271f38aede738d01523ad101643ab8e7e"
    client_secret = "7b310bac07a52c552589d2f9166c9873fadbc186141edac1c2892e63568c5fff"
    sdk_client = MediaMatchSDKClient(client_id, client_secret)

    batch_id = 7350887631447785478
    # STEP 2: Check the delivery status, this can take up to an hour until it become success
    try:
        delivery_status = sdk_client.video_upload_service.get_delivery_status(batch_id)
        print(delivery_status)
    except Exception as e:
        print(f"An error occurred querying delivery status: {e}")

if __name__ == "__main__":
    main()
