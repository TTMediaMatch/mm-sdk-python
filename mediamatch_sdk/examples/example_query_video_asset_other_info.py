from mediamatch_sdk.client import MediaMatchSDKClient

def main():
    # STEP 1: Initialize the SDK
    client_id = "cli_ee1a59258ae8c1601a4c0eb5f2da66b0f63fcb8c5ec91a451ad544b37677be91"
    client_secret = "caa970543a82aaa7eeeadf85f62c57146f6f2c0dfee8f65570e11aaaa3824a91"
    sdk_client = MediaMatchSDKClient(client_id, client_secret)

    asset_id = 7219207559314931717
    # STEP 2: Retrieve asset relevant information:
    # asset's creation time, content category, source, status (active, inactive, needs review),
    # recent views for the VOD scan (past 7 days total views, 0 views for the live scan,
    # number of matches on the VOD scan, number of matches on the live scan,
    # reference overlaps & the other RH's names with overlaps.
    try:
        asset_other_info = sdk_client.video_asset_service.get_video_asset_other_info(asset_id)
        print(asset_other_info)
    except Exception as e:
        print(f"An error occurred getting the other information of this asset: {e}")

if __name__ == "__main__":
    main()