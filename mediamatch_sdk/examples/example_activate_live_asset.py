from mediamatch_sdk.client import MediaMatchSDKClient

def main():
    # STEP 1: Initialize the SDK
    client_id = "cli_fcf0a39c9d04e22bdccf5c8f7e4b94c271f38aede738d01523ad101643ab8e7e"
    client_secret = "7b310bac07a52c552589d2f9166c9873fadbc186141edac1c2892e63568c5fff"
    sdk_client = MediaMatchSDKClient(client_id, client_secret)

    asset_id = 7219207559314931717
    # STEP 2: Create an activate job, http status code return 200 means success.
    try:
        activate_status = sdk_client.live_asset_service.activate_live_asset(asset_id)
        print(activate_status)
    except Exception as e:
        print(f"An error occurred activating the asset: {e}")

if __name__ == "__main__":
    main()