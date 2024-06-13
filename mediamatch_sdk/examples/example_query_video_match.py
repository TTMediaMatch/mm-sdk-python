import time

from mediamatch_sdk.client import MediaMatchSDKClient

def main():
    # STEP 1: Initialize the SDK
    client_id = "cli_fcf0a39c9d04e22bdccf5c8f7e4b94c271f38aede738d01523ad101643ab8e7e"
    client_secret = "7b310bac07a52c552589d2f9166c9873fadbc186141edac1c2892e63568c5fff"
    sdk_client = MediaMatchSDKClient(client_id, client_secret)

    asset_id = 7205466028057395205
    # 2024-03-10 00:00:00
    start_time = 1710000000
    # 2024-04-10 00:00:00
    end_time = 1712678400
    page = 1
    pageSize = 50
    # STEP 2: Retrieve asset match information
    try:
        matchs = sdk_client.video_asset_service.get_video_match(asset_id,start_time,end_time,page,pageSize)
        print(matchs)
    except Exception as e:
        print(f"An error occurred querying delivery status: {e}")

    # without page and pageSize, default value is page=1,pageSize=50
    try:
        matchs = sdk_client.video_asset_service.get_video_match(asset_id,start_time,end_time)
        print(matchs)
    except Exception as e:
        print(f"An error occurred querying delivery status: {e}")

if __name__ == "__main__":
    main()
