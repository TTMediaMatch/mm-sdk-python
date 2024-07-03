from mediamatch_sdk.client import MediaMatchSDKClient

def main():
    # STEP 1: Initialize the SDK
    client_id = "cli_ee1a59258ae8c1601a4c0eb5f2da66b0f63fcb8c5ec91a451ad544b37677be91"
    client_secret = "caa970543a82aaa7eeeadf85f62c57146f6f2c0dfee8f65570e11aaaa3824a91"
    sdk_client = MediaMatchSDKClient(client_id, client_secret)

    asset_id = 7219207559314931717
    # STEP 2: Create an activate job, http status code return 200 means success.
    try:
        activate_status = sdk_client.video_asset_service.activate_video_asset(asset_id)
        print(activate_status)
    except Exception as e:
        print(f"An error occurred activating the asset: {e}")

if __name__ == "__main__":
    main()